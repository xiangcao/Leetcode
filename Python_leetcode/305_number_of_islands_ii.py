"""
Refer:
https://leetcode.com/discuss/69392/python-clear-solution-unionfind-class-weighting-compression

https://leetcode.com/discuss/69488/compact-python

"""
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
    
        ans=[]
        islands = UF()
        for p in map(tuple, positions):
            islands.add(p)
            for direction in (1,0), (-1, 0), (0, 1), (0,-1):
                q = (p[0] + direction[0], p[1] + direction[1])
                if q in islands.id:
                    islands.union(p,q)
            ans.append(islands.count)
        return ans
        
class UF(object):
    def __init__(self):
        self.id = {}
        self.rank={}
        self.count = 0
    def find(self, x):
        if self.id[x] != x:
            self.id[x] = self.find(self.id[x])
        return self.id[x]
    def union(self, x,y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] > self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.id[rootX] = rootY
        self.rank[rootY] += self.rank[rootY] == self.rank[rootX]
        self.count -= 1
    def add(self, x):
        self.id[x] = x
        self.rank[x] = 1
        self.count += 1

