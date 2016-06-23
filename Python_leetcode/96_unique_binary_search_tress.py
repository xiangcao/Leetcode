class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        sum = 0
        for i in range(1,n+1):
            sum += self.numTrees(i-1) + self.numTrees(n-i)
        return sum
        
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        sum = 0
        for i in range(1,n+1):
            sum += self.numTrees(i-1) * self.numTrees(n-i)
        return sum
    result={0:1, 1:1}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.result:
            return self.result[n]
        sum = 0
        for i in range(1,n+1):
            sum += self.numTrees(i-1) * self.numTrees(n-i)
        self.result[n] = sum
        return self.result[n]
