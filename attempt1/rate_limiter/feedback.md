# Rate Limiter Feedback

This feedback covers both phases in this folder. The reference implementations
below preserve the problem's FIFO queue behavior: requests that do not fit stay
queued, and later requests do not overtake them.

## Phase 1: Per-second limit

### What is working

- The deque is a good fit for a FIFO queue: requests are appended at the back
  and removed from the front efficiently.
- `emitAPI()` correctly stops when the next request would exceed the per-second
  limit, leaving it and all later requests queued.
- The examples cover batching, carrying requests into the next second, an empty
  queue, a zero limit, and a request that is too large.

### What to improve

- `requestAPI()` accepts negative costs. A negative cost can reduce the running
  total and let later requests exceed the actual limit. Reject invalid costs
  when they enter the queue.
- The error says the limit "must be positive", but the code allows `limit == 0`.
  That is valid and useful if zero-cost requests are allowed; the error should
  say non-negative, and the cost policy should be consistent.
- A request whose cost is greater than the limit will remain at the head of
  the FIFO queue forever and block every request behind it. This matches the
  current FIFO/keep-queued behavior, but call it out explicitly. If the desired
  product behavior is to skip or reject such requests, that policy needs to be
  agreed on rather than silently changing queue order.
- The complexity comment is imprecise: `emitAPI()` is O(k), where `k` is the
  number of requests it removes in that call (O(n) worst case); queued storage
  is O(n).
- Top-level `assert` statements are useful quick checks, but they are not a
  substitute for a test suite: assertions can be disabled with Python's
  optimization flag, and they do not organize boundary cases or failures.

### Reference solution

```python
from collections import deque


class APILimiter:
    def __init__(self, limit: int) -> None:
        if limit < 0:
            raise ValueError("limit must be non-negative")
        self.limit = limit
        self.q: deque[int] = deque()

    def requestAPI(self, cost: int) -> None:
        if cost < 0:
            raise ValueError("request cost must be non-negative")
        self.q.append(cost)

    def emitAPI(self) -> list[int]:
        emitted: list[int] = []
        total_cost = 0

        while self.q and total_cost + self.q[0] <= self.limit:
            cost = self.q.popleft()
            emitted.append(cost)
            total_cost += cost

        return emitted
```

## Phase 2: Sliding-window limit

### What is working

- The code uses a FIFO queue and correctly checks the pending request against
  the budget left after previously emitted costs.
- It keeps costs grouped by second, which is the right information to track
  for a sliding-window limit.
- The main example exercises requests that must wait for earlier costs to
  expire.

### What to fix

- **Time must advance on every `emitAPI()` call, including when the request
  queue is empty.** The early `return []` skips the window update. I verified
  this sequence against the supplied implementation:

  ```python
  limiter = WindowRateLimit(limit=5, window=3)
  limiter.requestAPI(4)
  limiter.emitAPI()  # [4]
  limiter.emitAPI()  # []
  limiter.emitAPI()  # []
  limiter.requestAPI(3)
  limiter.emitAPI()  # Current code: []; expected: [3]
  ```

  Since each call represents a second, the cost from the first second should
  have expired by the fourth call. An empty second still needs to be recorded
  as a zero-cost second.
- The final test constructs `WindowRateLimit(0, 0)`, but the constructor
  rejects both values. Running the supplied file raises `ValueError` at that
  test, so the assertion immediately after it is unreachable. A zero-length
  window is undefined and should be rejected; a zero limit can be supported
  consistently with Phase 1.
- Request costs are not validated. Negative costs can corrupt the rolling
  budget and allow the limit to be exceeded.
- `sum(self.prev_window)` recalculates the historical total every second,
  making each call O(window) before processing requests. Keep a running total
  so rolling the window is O(1); request processing is O(k) for the requests
  emitted that second.
- The current tests do not cover empty seconds followed by new requests, which
  is why the skipped-window bug is missed.

### Reference solution

Each call to `emitAPI()` represents one elapsed second. The history contains
the costs from the preceding `window - 1` seconds; the current second is
accounted for while selecting requests. Empty calls still roll the history
forward.

```python
from collections import deque


class WindowRateLimit:
    def __init__(self, limit: int, window: int) -> None:
        if limit < 0:
            raise ValueError("limit must be non-negative")
        if window <= 0:
            raise ValueError("window must be positive")

        self.limit = limit
        self.window = window
        self.q: deque[int] = deque()
        self.previous_costs: deque[int] = deque([0] * (window - 1))
        self.previous_total = 0

    def requestAPI(self, cost: int) -> None:
        if cost < 0:
            raise ValueError("request cost must be non-negative")
        self.q.append(cost)

    def emitAPI(self) -> list[int]:
        emitted: list[int] = []
        remaining = self.limit - self.previous_total
        current_total = 0

        while self.q and self.q[0] <= remaining:
            cost = self.q.popleft()
            emitted.append(cost)
            remaining -= cost
            current_total += cost

        # Record this second even when no requests were emitted.
        if self.window > 1:
            expired = self.previous_costs.popleft()
            self.previous_total -= expired
            self.previous_costs.append(current_total)
            self.previous_total += current_total

        return emitted
```

The history update also works for `window == 1`: there are no previous seconds
to retain, so only the current second's costs constrain that call.

### Follow-up tests worth adding

- Phase 1: zero limit with zero-cost requests; negative limit; negative request
  cost; oversized request at the front of the queue.
- Phase 2: `window == 1`; zero limit; negative cost; an empty second that
  expires old cost before a new request; a request that fits exactly at the
  window-expiry boundary.
- For both phases, assert that requests remain in FIFO order and that emitted
  costs never exceed the applicable limit.
