"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Constraints:

costs.length == n
costs[i].length == 3
0 <= n <= 100
1 <= costs[i][j] <= 20
"""
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        
        dp[0] = costs[0]
        
        for i in range(1, n):
            for j in range(3):
                 dp[i][j] = costs[i][j] + min(dp[i-1][k] for k in range(3) if k != j)
        return min(dp[n-1][j] for j in range(3))
