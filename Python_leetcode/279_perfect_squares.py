class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Accepted
        #BFS refer: https://leetcode.com/discuss/62229/short-python-solution-using-bfs

        if n < 2:
            return n
        squares = [i*i for i in range(1, int(math.sqrt(n))+1)] 
        
        cnt =  0 
        target = {n}
        while target:
            cnt += 1
            childLevel = set()
            for targetNum in target:
                for s in squares:
                    if targetNum == s:
                        return cnt
                    if targetNum < s:
                        break
                    else:
                        childLevel.add(targetNum - s)
            target = childLevel
        return cnt
                 
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #refer https://leetcode.com/discuss/58056/summary-of-different-solutions-bfs-static-and-mathematics
        # Dynamic Programming  Time limit exceeded 
        # minCount[i]: min number of squares that sum to i
        minCount = [i for i in range(n+1)]
        
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                minCount[i] = min(minCount[i], minCount[i-j*j] + 1)
                j += 1
        return minCount[n]
            
            
