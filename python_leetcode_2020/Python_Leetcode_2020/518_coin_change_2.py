"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""

class Solution:
    """
    Time complexity: \mathcal{O}(N \times \textrm{amount})O(N×amount), where N is a length of coins array.
    Space complexity: \mathcal{O}(\textrm{amount})O(amount) to keep dp array.
    """
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]



This is a classic knapsack problem. Honestly, I'm not good at knapsack problem, it's really tough for me.

dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
State transition:

not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]
Initialization: dp[i][0] = 1

Once you figure out all these, it's easy to write out the code:

    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length+1][amount+1];
        dp[0][0] = 1;
        
        for (int i = 1; i <= coins.length; i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= amount; j++) {
                dp[i][j] = dp[i-1][j] + (j >= coins[i-1] ? dp[i][j-coins[i-1]] : 0);
            }
        }
        return dp[coins.length][amount];
    }
Now we can see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]], then we can optimize the space by only using one-dimension array.

    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i-coin];
            }
        }
        return dp[amount];
    }
