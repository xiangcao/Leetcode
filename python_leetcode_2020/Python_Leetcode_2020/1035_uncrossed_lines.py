java:
class Solution {
    public int maxUncrossedLines(int[] A, int[] B) {
        int m = A.length, n = B.length, dp[] = new int[n+1];
        for (int i = 1; i <= m; ++i)
            for (int j = 1, prev = 0; j <= n; ++j){
                int temp = dp[j];
                if (A[i-1] == B[j-1])
                    dp[j] = 1 + prev;
                else
                    dp[j] =  Math.max(dp[j], dp[j-1]);
                prev = temp;
            }
        return dp[n];
    }
}


python:
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [0] * (n+1)
        
        for i in range(1, m+1):
            prev = 0
            for j in range(1, n+1):
                temp = dp[j]
                if A[i-1] == B[j-1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j-1], dp[j])
                prev = temp

        return dp[n]

