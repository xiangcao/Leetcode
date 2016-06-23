class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [1 for i in range(n)]

        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    count[j] = 1
                else:
                    count[j] = count[j] + count[j-1]
        return count[n-1]
        
