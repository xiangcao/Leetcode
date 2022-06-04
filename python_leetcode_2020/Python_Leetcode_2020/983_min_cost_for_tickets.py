#DP
"""
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
# Recurisve with memoization
# 1. Day variant: calculate cost for each calendar
# For each day, if you don't have to travel today, then it's strictly better to wait to buy a pass. If you have to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or 30-day pass.
# We can express those choices as a recursion and use dynamic programming. Let's say dp(i) is the cost to fulfill your travel plan from day i to the end of the plan. Then, if you have to travel today, your cost is:
# dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
# Time: O(365), Space: O(365)
from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)

# 2. Travel day: calculate cost for each travel day
# As in Approach 1, we only need to buy a travel pass on a day we intend to travel.
# Now, let dp(i) be the cost to travel from day days[i] to the end of the plan. If say, j1 is the largest index such that days[j1] < days[i] + 1, j7 is the largest index such that days[j7] < days[i] + 7, and j30 is the largest index such that days[j30] < days[i] + 30, then we have:
# dp(i)=min(dp(j1)+costs[0],dp(j7)+costs[1],dp(j30)+costs[2])

# Time O(N), Space O(N), N is the travel days
from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i): # How much money to do days[i]+
            if i >= N: return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans

        return dp(0)


# DP 
"""
Intuition
For each travel day, we can buy a one-day ticket, or use 7-day or 30-day pass as if we would have purchased it 7 or 30 days ago. We need to track rolling costs for at least 30 days back, and use them to pick the cheapest option for the next travel day.

Here, we can use two approaches: track cost for all calendar days, or process only travel days. The first approach is simpler to implement, but it's slower. Since the problem is limited to one calendar year, it does not make much of a difference; for a generalized problem I would recommend the second approach.

1. Track calendar days
We track the minimum cost for all calendar days in dp. For non-travel days, the cost stays the same as for the previous day. For travel days, it's a minimum of yesterday's cost plus single-day ticket, or cost for 8 days ago plus 7-day pass, or cost 31 days ago plus 30-day pass.
int mincostTickets(vector<int>& days, vector<int>& costs) {
  unordered_set<int> travel(begin(days), end(days));
  int dp[366] = {};
  for (int i = 1; i < 366; ++i) {
    if (travel.find(i) == travel.end()) dp[i] = dp[i - 1];
    else dp[i] = min({ dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2]});
  }
  return dp[365];
}
Optimizations
In the previous solution, we store cost for all calendar days. However, since we only look 30 days back, we can just store the cost for last 30 days in a rolling array.

In addition, we can only look at calendar days within our first and last travel dates, as @zengxinhai suggested.
int mincostTickets(vector<int>& days, vector<int>& costs) {
  unordered_set<int> travel(begin(days), end(days));
  int dp[30] = {};
  for (int i = days.front(); i <= days.back(); ++i) {
    if (travel.find(i) == travel.end()) dp[i % 30] = dp[(i - 1) % 30]; # on non-traveld ays, the cost stays the same as for the previous day;
    else dp[i % 30] = min({ dp[(i - 1) % 30] + costs[0],
        dp[max(0, i - 7) % 30] + costs[1], dp[max(0, i - 30) % 30] + costs[2] });
  }
  return dp[days.back() % 30];
}
Complexity analysis
Time Complexity: O(N), where N is the number of calendar days.
Space Complexity: O(N) or O(31) for the optimized solution. Stricter, it's a maximum duration among all pass types.


2.Track travel days
We track the minimum cost for each travel day. We process only travel days and store {day, cost} for 7-and 30-day passes in the last7 and last30 queues. After a pass 'expires', we remove it from the queue. This way, our queues only contains travel days for the last 7 and 30 days, and the cheapest pass prices are in the front of the queues.
int mincostTickets(vector<int>& days, vector<int>& costs, int cost = 0) {
  queue<pair<int, int>> last7, last30;
  for (auto d : days) {
    while (!last7.empty() && last7.front().first + 7 <= d) last7.pop();
    while (!last30.empty() && last30.front().first + 30 <= d) last30.pop();
    last7.push({ d, cost + costs[1] });
    last30.push({ d, cost + costs[2] });
    cost = min({ cost + costs[0], last7.front().second, last30.front().second });
  }
  return cost;
}
Complexity analysis
Time Complexity: O(n), where n is the number of travel days.
Space Complexity: O(38). Stricter, it's a sum of duration for all pass types (1 + 7 + 30 in our case).
