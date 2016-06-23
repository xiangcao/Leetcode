class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        
        for p in prices:
            minPrice = min(p, minPrice)
            maxProfit = max(maxProfit, p-minPrice)
        return maxProfit
