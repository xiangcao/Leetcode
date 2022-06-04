"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = float('inf')
        
        for p in prices:
            minPrice = min(minPrice, p)
            maxPro = max(maxPro, p-minPrice)
        return maxPro

# round 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = float("inf")
        ans = 0
        for p in prices:
            ans = max(ans, p - minsofar)
            minsofar = min(minsofar, p)
        return ans
