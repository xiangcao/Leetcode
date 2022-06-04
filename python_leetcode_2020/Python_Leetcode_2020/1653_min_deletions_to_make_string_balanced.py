"""
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'
"""
# DP
class Solution {
    public int minimumDeletions(String s) {
        int l = s.length();
		//dp stores number of chars to remove to make s.substring(0, i) valid
        int[] dp = new int[l + 1];
        int bcount = 0;
        for (int i = 0; i < l; i++) {
            if (s.charAt(i) == 'a') {
                //case 1: keep current a. ==> prev chars must be a...a
                //so need to remove all 'b' chars before i, which is bcount
                
                //case 2: remove current a ==> prev chars must be a...ab...b
                //so need to remove current a and whatever makes substring before current i valid which is dp[i];
                dp[i + 1] = Math.min(dp[i] + 1, bcount);
            } else {
                //since it is always valid to append 'b' if substring before current i is valid, so just copy whatever makes substring before i valid which is dp[i];
                dp[i + 1] = dp[i];
                bcount++;
            }
        }
        
        return dp[l];
    }
}

# greedy
class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = 0
        count = 0
        for c in s:
            if c == 'b':
                count += 1
            if c == 'a':
                if count > 0:
                    count -= 1
                    result += 1
        return result
