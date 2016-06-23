class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        results = []
        results.append(0)
        for i in range(1,num+1):
            prev = i >> 1
            lastdigit = i & 1
            results.append(results[prev] + lastdigit)
        return results
            
