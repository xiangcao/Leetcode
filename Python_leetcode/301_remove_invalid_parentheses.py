"""
 Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

Credits:
Special thanks to @hpplayer for adding this problem and creating all test cases.
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        par = ['(', ')']
        #refer this solution: https://leetcode.com/discuss/81478/easy-short-concise-and-fast-java-dfs-3-ms-solution

        #special test case "()k)))". so we need last_j
        def remove(s, ans, lasti, lastj, index):
            count = 0
            for i in range(lasti, len(s)):
                if s[i] == par[index]:
                    count += 1
                elif s[i] == par[1-index]:
                    count -= 1
                if count < 0 :
                    # remove a ) from the prefix
                    for j in range(lastj, i+1):
                        if s[j] == par[1-index] and (j == 0 or s[j-1] != par[1-index]):
                            remove(s[:j]+s[j+1:], ans, i, j, index)
                    return
            reversedS = s[::-1]
            if par[index] == '(':
                remove(reversedS, ans, 0, 0, 1-index)
            else:
                ans.append(reversedS)
                    
        remove(s, ans, 0, 0, 0)
        return ans
            
        
        
"""
public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> ans = new ArrayList<>();
        remove(s, ans, 0, 0, new char[]{'(', ')'});
        return ans;
    }
    
    //special test case "()k)))". so we need last_j
    public void remove(String s, List<String> ans, int last_i, int last_j,  char[] par) {
        for (int stack = 0, i = last_i; i < s.length(); ++i) {
            if (s.charAt(i) == par[0]) stack++;
            if (s.charAt(i) == par[1]) stack--;
            if (stack >= 0) continue;
            for (int j = last_j; j <= i; ++j)
                if (s.charAt(j) == par[1] && (j == last_j || s.charAt(j - 1) != par[1]))   
                    remove(s.substring(0, j) + s.substring(j + 1, s.length()), ans, i, j, par);
            return;
        }
        String reversed = new StringBuilder(s).reverse().toString();
        if (par[0] == '(') // finished left to right
            remove(reversed, ans, 0, 0, new char[]{')', '('});
        else // finished right to left
            ans.add(reversed);
    }
}
"""
        
