class DSU1:
    def __init__(self, N):
        self.par = [-1 for _ in range(N)]
    def find(self, x):
        if self.par[x] == -1:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY: #Required when parent pointing to -1 indicates the node is root
            self.par[parentX] = parentY

class DSU:
    def __init__(self, N):
        self.par = [_ for _ in range(N)]
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        # if parentX != parentY: # Not required when parent pointing to itself indicates the node is root
        self.par[parentX] = parentY

class Solution(object): # (NW) * min(N, W*W) complexity
    def numSimilarGroups(self, A: List[str]) -> int :
        N, W = len(A), len(A[0])

        def similar(word1, word2):
            diff = 0
            for x, y in zip(word1, word2):
                if x != y:
                    diff += 1
                    if diff > 2:
                        return False
            return diff <= 2

        def combination(A):
            for i in range(len(A)-1):
                for j in range(i+1, len(A)):
                    yield ((i, A[i]), (j, A[j]))
        
        dsu = DSU(N)

        if N < W*W: # If few words, then check for pairwise similarity: O(N^2 W)
            for (i1, word1), (i2, word2) in combination(A):
                    #itertools.combinations(enumerate(A), 2):
                if similar(word1, word2):
                    dsu.union(i1, i2)

        else: # If short words, check all neighbors: O(N W^3)
            buckets = collections.defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j0, j1 in itertools.combinations(range(W), 2):
                    L[j0], L[j1] = L[j1], L[j0]
                    buckets["".join(L)].add(i)
                    L[j0], L[j1] = L[j1], L[j0]

            for i1, word in enumerate(A):
                for i2 in buckets[word]:
                    dsu.union(i1, i2)

        return sum(dsu.par[x] == x for x in range(N))
