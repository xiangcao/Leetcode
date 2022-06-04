"""
Your music player contains N different songs and she wants to listen to L (not necessarily different) songs during your trip.  You create a playlist so that:

Every song is played at least once
A song can only be played again only if K other songs have been played
Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
Example 2:

Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
Example 3:

Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
"""

class Solution:
"""Intuition

Let dp[i][j] be the number of playlists of length i that have exactly j unique songs. We want dp[L][N], and it seems likely we can develop a recurrence for dp.

Algorithm

Consider dp[i][j]. Last song, we either played a song for the first time or we didn't. If we did, then we had dp[i-1][j-1] * (N-j+1) ways to choose it. If we didn't, then we repeated a previous song in dp[i-1][j] * max(j-K, 0) ways (j of them, except the last K ones played are banned.)
"""
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i-1, j-1) * (N-j+1)
            ans += dp(i-1, j) * max(j-K, 0)
            return ans % (10**9+7)

        return dp(L, N)

 # bottom up DP
    public int numMusicPlaylists(int N, int L, int K) {
        int mod = (int)Math.pow(10, 9) + 7;
        long[][] dp = new long[L+1][N+1];
        dp[0][0] = 1;
        for (int i = 1; i <= L; i++){
            for (int j = 1; j <= N; j++){
                dp[i][j] = (dp[i-1][j-1] * (N - (j-1)))%mod; 
                if (j > K){
                    dp[i][j] = (dp[i][j] + (dp[i-1][j] * (j-K))%mod)%mod;
                }
            }
        }
        return (int)dp[L][N];
    }
}

"""solution 2
F(N,L,K) = F(N - 1, L - 1, K) * N + F(N, L - 1, K) * (N - K)

F(N - 1, L - 1, K)
If only N - 1 in the L - 1 first songs.
We need to put the rest one at the end of music list.
Any song can be this last song, so there are N possible combinations.

F(N, L - 1, K)
If already N in the L - 1 first songs.
We can put any song at the end of music list,
but it should be different from K last song.
We have N - K choices.

Time Complexity:
O((L-K)(N-K))

def numMusicPlaylists(self, N, L, K):
        dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
        return dp[N][L] % (10**9 + 7)
