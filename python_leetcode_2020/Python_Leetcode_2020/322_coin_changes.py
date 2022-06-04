"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    # DP;  dp[i]: minimum number of coins to make up amount i
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for x in range(amount + 1):
            for coin in coins:
                if x >= coin:
                    dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
    #DP2,also accepted
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 


class Solution {
  # brute force
  public int coinChange1(int[] coins, int amount) {
    return coinChange(0, coins, amount, new int[coins.length][amount]);
  }

  private int coinChange(int idxCoin, int[] coins, int amount, int [][] count) {
    if (amount < 0) return -1;
    if (amount == 0)
      return 0;
    if (idxCoin < coins.length && amount > 0) {
      if (count[idxCoin][amount-1] != 0) return count[idxCoin][amount-1];
      int maxVal = amount/coins[idxCoin];
      int minCost = Integer.MAX_VALUE;
      for (int x = 0; x <= maxVal; x++) {
        if (amount >= x * coins[idxCoin]) {
          int res = coinChange(idxCoin + 1, coins, amount - x * coins[idxCoin], count);
          if (res != -1)
            minCost = Math.min(minCost, res + x);
        }
      }
      if (amount == 88) {
          idxCoin = idxCoin;
      }
      count[idxCoin][amount-1] = (minCost == Integer.MAX_VALUE)? -1: minCost;
      return count[idxCoin][amount-1];
    }
    return -1;
  }
    
  //Top down DP Memoization    
  public int coinChange(int[] coins, int amount) {
    if (amount < 1) return 0;
    return coinChange(coins, amount, new int[amount]);
  }

  private int coinChange(int[] coins, int rem, int[] count) {
    if (rem < 0) return -1;
    if (rem == 0) return 0;
    if (count[rem - 1] != 0) return count[rem - 1];
    int min = Integer.MAX_VALUE;
    for (int coin : coins) {
      int res = coinChange(coins, rem - coin, count);
      if (res >= 0 && res < min)
        min = 1 + res;
    }
    count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
    return count[rem - 1];
  }
}
