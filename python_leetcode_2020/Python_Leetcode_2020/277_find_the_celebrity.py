# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity1(self, n: int) -> int:
        candidate = n-1
        for i in range(n-1):
            if knows(candidate, i):
                candidate = i
        def isCelebrity(index):
            for i in range(n):
                if i == index: continue
                if knows(index, i) or not knows(i, index):
                    return False
            return True
        return candidate if isCelebrity(candidate) else -1
           
    # brute force O(N^2)
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            celebrity = True
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    celebrity=False
                    break
            if celebrity:
                return i
        return -1
    from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if self.cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue
            if self.cachedKnows(i, j) or not self.cachedKnows(j, i):
                return False
        return True

