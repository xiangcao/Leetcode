class Solution(object):
    def numWays(self, n, k):
        #https://segmentfault.com/a/1190000003790650
        #https://leetcode.com/problems/paint-fence/
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        count = [0] * 3
        count[0] = k 
        count[1] = k*k
        if n == 0:
            return 0
        if n < 3:
            return count[n-1]
        for i in range(2,n):
            count[2] = (k-1)*count[1]  + (k-1)*count[0] 
            count[0] = count[1]
            count[1] = count[2]
        return count[2]
            
            
