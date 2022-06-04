"""
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        i, buy, sell, profit = 0, 0, 0, 0
        N = len(prices)-1
        while i < N:
            while i < N and prices[i + 1] <= prices[i]:
                i += 1
            buy = prices[i]
            while i < N and prices[i + 1] > prices[i]:
                i+=1
            sell = prices[i]
            profit += sell - buy
        return profit
