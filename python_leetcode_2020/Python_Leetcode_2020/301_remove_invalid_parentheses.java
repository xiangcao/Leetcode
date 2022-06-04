"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).
"""
class Solution {
    //BFS
    public List<String> removeInvalidParentheses1(String s) {
      List<String> res = new ArrayList<>();

      // sanity check
      if (s == null) return res;

      Set<String> visited = new HashSet<>();
      Queue<String> queue = new LinkedList<>();

      // initialize
      queue.add(s);
      visited.add(s);

      boolean found = false;

      while (!queue.isEmpty()) {
        s = queue.poll();

        int valid = isValid(s);
        if (valid == 0) {
          // found an answer, add to the result
          res.add(s);
          found = true;
        }

        if (found) continue;

        // generate all possible states
        for (int i = 0; i < s.length(); i++) {
          // we only try to remove left or right paren
          if (s.charAt(i) != '(' && s.charAt(i) != ')') continue;
          if (valid > 0 && s.charAt(i) == ')') continue;
          if (valid < 0 && s.charAt(i) == '(') continue;
          String t = s.substring(0, i) + s.substring(i + 1);

          if (!visited.contains(t)) {
            // for each state, if it's not visited, add it to the queue
            queue.add(t);
            visited.add(t);
          }
        }
      }

      return res;
    }
    
    // helper function checks if string s contains valid parantheses
    int isValid(String s) {
      int count = 0;

      for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(') count++;
        if (c == ')') {
            count--;
            if (count < 0) return count;
        }
      }

      return count;
    }

    
    // Generate unique answer once and only once, do not rely on Set.
    // Do not need preprocess.
    /*
    Key Points:

    Generate unique answer once and only once, do not rely on Set.
    Do not need preprocess.
    Runtime 3 ms.
    Explanation:
    We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
    The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

    To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix. However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

    After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
    For this, we keep tracking the last removal position and only remove ‘)’ after that.

    Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
    The answer is: do the same from right to left.
    However a cleverer idea is: reverse the string and reuse the code!
    Here is the final implement in Java.*/
    public List<String> removeInvalidParentheses2(String s) {
        List<String> ans = new ArrayList<>();
        remove(s, ans, 0, 0, new char[]{'(', ')'});
        return ans;
    }

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

/////////////////////////////////////////////////////////////////////////////////
 
  private Set<String> validExpressions = new HashSet<String>();

  private void recurse(
      String s,
      int index,
      int leftCount,
      int rightCount,
      int leftRem,
      int rightRem,
      StringBuilder expression) {

    // If we reached the end of the string, just check if the resulting expression is
    // valid or not and also if we have removed the total number of left and right
    // parentheses that we should have removed.
    if (index == s.length()) {
      if (leftRem == 0 && rightRem == 0) {
        this.validExpressions.add(expression.toString());
      }

    } else {
      char character = s.charAt(index);
      int length = expression.length();

      // The discard case. Note that here we have our pruning condition.
      // We don't recurse if the remaining count for that parenthesis is == 0.
      if ((character == '(' && leftRem > 0) || (character == ')' && rightRem > 0)) {
        this.recurse(
            s,
            index + 1,
            leftCount,
            rightCount,
            leftRem - (character == '(' ? 1 : 0),
            rightRem - (character == ')' ? 1 : 0),
            expression);
      }

      expression.append(character);

      // Simply recurse one step further if the current character is not a parenthesis.
      if (character != '(' && character != ')') {

        this.recurse(s, index + 1, leftCount, rightCount, leftRem, rightRem, expression);

      } else if (character == '(') {

        // Consider an opening bracket.
        this.recurse(s, index + 1, leftCount + 1, rightCount, leftRem, rightRem, expression);

      } else if (rightCount < leftCount) {

        // Consider a closing bracket.
        this.recurse(s, index + 1, leftCount, rightCount + 1, leftRem, rightRem, expression);
      }

      // Delete for backtracking.
      expression.deleteCharAt(length);
    }
  }

  public List<String> removeInvalidParentheses(String s) {

    int left = 0, right = 0;

    // First, we find out the number of misplaced left and right parentheses.
    for (int i = 0; i < s.length(); i++) {

      // Simply record the left one.
      if (s.charAt(i) == '(') {
        left++;
      } else if (s.charAt(i) == ')') {
        // If we don't have a matching left, then this is a misplaced right, record it.
        right = left == 0 ? right + 1 : right;

        // Decrement count of left parentheses because we have found a right
        // which CAN be a matching one for a left.
        left = left > 0 ? left - 1 : left;
      }
    }

    this.recurse(s, 0, 0, 0, left, right, new StringBuilder());
    return new ArrayList<String>(this.validExpressions);
  }
}
