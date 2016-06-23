class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        inverse = False
        if n < 0:
            inverse = True
            n = -n
        root = self.myPow(abs(x), n/2)
        result = root * root
        if n%2 != 0:
            result *= x
        return 1/ result if inverse else result
        
        
