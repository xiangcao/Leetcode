"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?
"""
class Solution(object):
    # Time: O(nk^2); directly modified from paint house I
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        dp = [[0] * k for _ in range(n)]
        
        dp[0] = costs[0]
        
        for i in range(1, n):
            for j in range(k):
                 dp[i][j] = costs[i][j] + min(dp[i-1][k] for k in range(k) if k != j)
        return min(dp[n-1][j] for j in range(k))
    
    # Time: O(nk), Space O(1)
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0: return 0 # This is a valid case.
        k = len(costs[0])

        # Firstly, we need to determine the 2 lowest costs of
        # the first row. We also need to remember the color of
        # the lowest.
        prev_min_cost = prev_second_min_cost = prev_min_color = None
        for color, cost in enumerate(costs[0]):
            if prev_min_cost is None or cost < prev_min_cost:
                prev_second_min_cost = prev_min_cost
                prev_min_color = color
                prev_min_cost = cost
            elif prev_second_min_cost is None or cost < prev_second_min_cost:
                prev_second_min_cost = cost

        # And now, we need to work our way down, keeping track of the minimums.
        for house in range(1, n):
            min_cost = second_min_cost = min_color = None
            for color in range(k):
                # Determime cost for this cell (without writing it into input array.)
                cost = costs[house][color]
                if color == prev_min_color:
                    cost += prev_second_min_cost
                else:
                    cost += prev_min_cost
                # And work out whether or not it is a current minimum.
                if min_cost is None or cost < min_cost:
                    second_min_cost = min_cost
                    min_color = color
                    min_cost = cost
                elif second_min_cost is None or cost < second_min_cost:
                    second_min_cost = cost
            # Transfer currents to be prevs.
            prev_min_cost = min_cost
            prev_min_color = min_color
            prev_second_min_cost = second_min_cost

        return prev_min_cost
