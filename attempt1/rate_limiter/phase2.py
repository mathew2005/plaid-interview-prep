from collections import deque
class WindowRateLimit:

    def __init__(self,limit:int,window:int) -> None:
        if window <= 0 or limit <= 0:
            raise ValueError("Window and Limit must be non-negative values")
        self.limit = limit
        self.window = window
        self.prev_window = deque([0] * (window - 1))
        self.q = deque([])

    def requestAPI(self,request:int) -> None:
        self.q.append(request)

    def emitAPI(self) -> list:
        if not self.q: return []

        curr_cost = []
        window_cost = sum(self.prev_window)

        while self.q and window_cost + self.q[0] <= self.limit:
            curr = self.q.popleft()
            curr_cost.append(curr)
            window_cost += curr



        self.prev_window.popleft()
        self.prev_window.append(sum(curr_cost))
        
        return curr_cost

# edge cases:

"""
window size  = 0 , limit = 0, 
window size > limit (shouldn't be codependent), window size < limit (normal case)
window size <= 0, limit <= 0 (raise an error)
emit API before requestAPI (return [])
"""

# happy path
limit1 = 5
window1 = 3
api_limiter1 = WindowRateLimit(limit1,window1)
# t = 0
assert api_limiter1.requestAPI(4) == None
assert api_limiter1.requestAPI(3) == None
assert api_limiter1.requestAPI(3) == None
assert api_limiter1.emitAPI() ==  [4]
# t = 1
assert api_limiter1.emitAPI() ==  []
# t = 2
assert api_limiter1.emitAPI() ==  []
# t = 3
assert api_limiter1.emitAPI() ==  [3]
# t = 4
assert api_limiter1.emitAPI() ==  []
# t = 5
assert api_limiter1.emitAPI() ==  []
# t = 6
assert api_limiter1.emitAPI() ==  [3]


# multiple elements in curr_count
limit2 = 5
window2 = 3
api_limiter2 = WindowRateLimit(limit2,window2)
# t = 0
assert api_limiter2.requestAPI(4) == None
assert api_limiter2.requestAPI(1) == None
assert api_limiter2.requestAPI(3) == None
assert api_limiter2.emitAPI() ==  [4,1]
# t = 1
assert api_limiter2.emitAPI() ==  []
# t = 2
assert api_limiter2.emitAPI() ==  []
# t = 3
assert api_limiter2.emitAPI() ==  [3]

# extra emit when queue is empty
assert api_limiter2.emitAPI() == []


limit3 = 0
window3 = 0
api_limiter3 = WindowRateLimit(limit3,window3)
# t = 0
assert api_limiter3.requestAPI(4) == None
assert api_limiter3.requestAPI(1) == None
assert api_limiter3.requestAPI(3) == None
assert api_limiter3.emitAPI() ==  [4,1]
# t = 1
assert api_limiter3.emitAPI() ==  []
# t = 2
assert api_limiter3.emitAPI() ==  []
# t = 3
assert api_limiter3.emitAPI() ==  [3]

