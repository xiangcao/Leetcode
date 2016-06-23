class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        #dp is monotonically increasing
        for i in range(3, n+1):
            left  = 1
            right = i-left
            while left <= right:
                #dp[3] = 2 < 3
                dp[i] = max(dp[i], max(left, dp[left]) *  max(right, dp[right]))
                left += 1
                right = i - left
        return dp[n]
        # time complexity: 1 + 2 + 3 + 4 + n/2 = 
        
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3: return n - 1
        dp = [0] * (n + 1)
        dp[2], dp[3] = 2, 3  # although integerBreak(2) will return 1, integerBreak(3) return 2. we should use dp[2] = 2, dp[3]
        for x in range(4, n + 1):
            dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
        return dp[n]
#http://bookshadow.com/weblog/2016/04/19/leetcode-integer-break/      
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        return max([reduce(operator.mul, self.splitInt(n, m)) for m in range(2, n + 1)])
    
    #将整数n均摊为m个相差不超过1的整数，m从2到n进行枚举。
    def splitInt(self, n, m):
        quotient = n / m
        remainder = n % m
        return [quotient] * (m - remainder) + [quotient + 1] * remainder
        
#上面的代码复杂度实际上是O(n ^ 2)，可以将复杂度简化为O(n)。
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        return max([self.mulSplitInt(n, m) for m in range(2, n + 1)])
    
    def mulSplitInt(self, n, m):
        quotient = n / m
        remainder = n % m
        return quotient ** (m - remainder) * (quotient + 1) ** remainder
