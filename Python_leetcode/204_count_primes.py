class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        skipped=[False for i in range(n)]
        count = 1
        for i in range(3, n, 2):
            if not skipped[i]:
                count += 1
                if i >  math.sqrt(n):
                    continue
                for j in range(i*i, n, i):
                    skipped[j] = True
                    
        return count
            
