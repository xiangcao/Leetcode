"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

class Solution:
    # Solution 1: Two directional DP
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit
    
    # solution 2 One Pass. Simulation
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0
        
        for p in prices:
            t1_cost = min(t1_cost, p)
            t1_profit= max(t1_profit, p - t1_cost)
            
            t2_cost = min(t2_cost, p - t1_profit)
            t2_profit = max(t2_profit, p - t2_cost)
        return t2_profit
