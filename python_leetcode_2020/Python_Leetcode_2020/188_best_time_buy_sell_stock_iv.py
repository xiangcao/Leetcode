# make most k transactions. max profit.
"""
It's not difficult to get the DP recursive formula:

dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
For k transactions, on i-th day,
if we don't trade then the profit is same as previous day dp[k, i-1];
and if we bought the share on j-th day where j=[0..i-1], then sell the share on i-th day then the profit is prices[i] - prices[j] + dp[k-1, j-1] .
Actually j can be i as well. When j is i, the one more extra item prices[i] - prices[j] + dp[k-1, j] = dp[k-1, i] looks like we just lose one chance of transaction.


"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
         * dp[i, j] represents the max profit up until prices[j] using at most i transactions. 
         * dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
         *          = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
         * dp[0, j] = 0; 0 transactions makes 0 profit
         * dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
        """
        n = len(prices)
        if (n <= 1):
            return 0

        # if k >= n/2, then you can make maximum number of transactions.
        if (k >=  n/2):
            maxPro = sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))
            return maxPro

        dp = [[0] * (n) for i in range(k+1)]
        for i in range(1, k+1):
            localMax = dp[i-1][0] - prices[0];
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1],  prices[j] + localMax)
                localMax = max(localMax, dp[i-1][j] - prices[j])
        return dp[k][n-1];

#Time O(K*N); Space O(K*N);
        public int MaxProfitDpCompact1T(int[] prices) {
            if (prices.Length == 0) return 0;
            var dp = new int[3, prices.Length];
            var min = new int[3];
            Array.Fill(min, prices[0]);
            for (int i = 1; i < prices.Length; i++) {
                for (int k = 1; k <= 2; k++) {
                    min[k] = Math.Min(min[k], prices[i] - dp[k-1, i-1]);
                    dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min[k]);
                }
            }

            return dp[2, prices.Length - 1];
        }

# optimize space to O(K):
        public int MaxProfitDpCompact2(int[] prices) {
            if (prices.Length == 0) return 0;
            var dp = new int[3];
            var min = new int[3];
            Array.Fill(min, prices[0]);
            for (int i = 1; i < prices.Length; i++)  {
                for (int k = 1; k <= 2; k++) {
                    min[k] = Math.Min(min[k], prices[i] - dp[k-1]);
                    dp[k] = Math.Max(dp[k], prices[i] - min[k]);
                }
            }

            return dp[2];
        }
#Python
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] * (k+1)
        mincost = [prices[0]] * (k+1)
        for i in range(1, len(prices)):
            for j in range(1, k+1):
                mincost[j] = min(mincost[j], prices[i]-dp[j-1])
                dp[j] = max(dp[j], prices[i] - mincost[j])
        return dp[-1]

# expand the array to all  named variables when k=2 
        public int MaxProfitDpCompactFinal(int[] prices)  {
            int buy1 = int.MaxValue, buy2 = int.MaxValue;
            int sell1 = 0, sell2 = 0;

            for (int i = 0; i < prices.Length; i++) {
                buy1 = Math.Min(buy1, prices[i]);
                sell1 = Math.Max(sell1, prices[i] - buy1);
                buy2 = Math.Min(buy2, prices[i] - sell1);
                sell2 = Math.Max(sell2, prices[i] - buy2);
            }

            return sell2;
        }
