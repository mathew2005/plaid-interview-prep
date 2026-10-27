# limit -> max total cost of request (given time window)
# request has an associated cost

# edge cases:
# what if api queue is empty (ie emitAPI asks for more than waht is currently avaialable) -> or if queue is empty
# what if limit is not full
from collections import deque
class APILimiter:
    def __init__(self,limit:int) -> None:
        if limit < 0:
            raise ValueError("limit must be positive")
        self.q = deque([])
        self.limit = limit

    def requestAPI(self,cost):
        self.q.append(cost)

    def emitAPI(self):
        total_cost, emitted = 0, []
        while self.q:
            next_cost = self.q[0]
            if total_cost + next_cost > self.limit:
                break
            
            curr_cost = self.q.popleft()
            
            emitted.append(curr_cost)
            total_cost += curr_cost

        return emitted

limit1 = 5
apiLimiter1 = APILimiter(limit1)

apiLimiter1.requestAPI(3)
apiLimiter1.requestAPI(2)
apiLimiter1.requestAPI(1)
apiLimiter1.requestAPI(1)

assert apiLimiter1.emitAPI() == [3,2]  # [3, 2]

apiLimiter1.requestAPI(2)

assert apiLimiter1.emitAPI() == [1,1,2]  # [1, 1, 2]

# empty list of request
assert apiLimiter1.emitAPI() == []  # []

# one request is bigger than the entire limit
limit2 = 5
apiLimiter2 = APILimiter(limit2)

apiLimiter2.requestAPI(13)
apiLimiter2.requestAPI(2)
apiLimiter2.requestAPI(1)
apiLimiter2.requestAPI(1)

assert apiLimiter2.emitAPI() == []  # []

# both request and limit are 0
limit3 = 0
apiLimiter3 = APILimiter(limit3)

apiLimiter3.requestAPI(0)
apiLimiter3.requestAPI(2)
apiLimiter3.requestAPI(1)
apiLimiter3.requestAPI(1)

assert apiLimiter3.emitAPI() ==  [0] # [0]
# time: O(n) -> iterate through q (of len n)
# space : O(n) -> amount of requests stored in the q