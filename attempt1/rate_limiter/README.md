
# API Rate Limiter

## Problem Description

Implement a rate limiter with the following behavior:

You are given a rate limit value `limit`, which represents the maximum total cost of requests that can be executed within a given time window.

Each request has an associated cost, and you can call the function `requestAPI(cost)` multiple times within a second to enqueue requests.

At the end of each second, the system calls `emitAPI()`, which returns an array of requests that can be executed in that second.

The total cost of the executed requests must not exceed the rate limit. Any remaining requests should stay queued and be considered in subsequent seconds.

---

## Part 1: Per-Second Rate Limiting

The rate limit applies per second.

- `requestAPI(cost)` enqueues a request with the given cost.
- `emitAPI()` returns the list of requests that can be executed this second without exceeding the per-second rate limit.

### Example

```python
limit = 5

requestAPI(3)
requestAPI(2)
requestAPI(1)
requestAPI(1)

emitAPI()  # [3, 2]

requestAPI(2)

emitAPI()  # [1, 1, 2]
```

---

## Part 2: Sliding Window Rate Limiting

Extend the system to support a sliding time window constraint.

You are given two parameters:

- `limit`: The maximum total cost allowed within any continuous `window` seconds.
- `window`: The size of the sliding window in seconds.

At each second, `emitAPI()` should return the list of requests that can be executed in that second, ensuring that the sum of costs for all executed requests in the past `window` seconds (including the current one) does not exceed `limit`.

### Example

```python
limit = 5
window = 3

# t = 0
requestAPI(4)
requestAPI(3)
requestAPI(3)
emitAPI()  # [4]

# t = 1
emitAPI()  # []

# t = 2
emitAPI()  # []

# t = 3
emitAPI()  # [3]

# t = 4
emitAPI()  # []

# t = 5
emitAPI()  # []

# t = 6
emitAPI()  # [3]
```
