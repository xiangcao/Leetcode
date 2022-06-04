class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = pow(10, 9) + 7
        color3 = 6
        color2 = 6

        for i in range(1, n):
            tempColor3 = color3
            color3 = (2 * color3 + 2 * color2) % MOD
            color2 = (2 * tempColor3 + 3 * color2) % MOD

        return int((color3 + color2) % MOD)
