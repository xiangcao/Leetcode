class Solution:
    # Time exceeded
    def numTrees1(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 1
        sum = 0
        for i in range(1, n+1):
            sum += self.numTrees(i-1) * self.numTrees(n-i)
        return sum

    def numTrees(self, n: int) -> int:
        total = [0] * (n+1)
        total[0], total[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                total[i] += total[j-1] * total[i-j]
        return total[n]
