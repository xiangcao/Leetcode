Idea is to keep track of how many * you have seen so far, and also of how many of those * you used as closing paranthesis. Go greedy on completing valid sequences, either with ) or using *.

When we greedily use * to complete one (), we might actually break up the existing valid pair in the sequence. And hence we might alienate one ), which could have matched with current (. So we need to account for that.

some, informal, description on steps:

start from the left- keep pushing all ( into stack.
When you encounter ):
if stack not empty, pop one element: (Stack will only have ( parantheses)
if stack is empty, then check if we have seen (or used) any * so far:
if yes, we can let go of this ) and decrement count for *
otherwise return false
When you encounter *:
increment count for *
if stack contains elements:
pop one element to complete valid sequence, and increment count for * again: cuz we used one ( (and might have broken existing valid pair in the sequence)
At the end, stack should be emtpy for a valid string, as usual
Here is implementation of my algo:

class Solution {
    // 1 ms
    public boolean checkValidString(String s) {
        Deque<Character> stk = new ArrayDeque<>();
        int scount = 0;
        for(char c : s.toCharArray()) {
            if(c == '(') stk.push(c);
            else {
                if (c == '*') {
                    scount++;
                    if(!stk.isEmpty()) {
                        stk.pop();
                        scount++;
                    }
                }  // "()"
                else if(!stk.isEmpty()) stk.pop();
                else if(scount > 0) scount--;
                else return false;
            }
        }
        return stk.isEmpty();
    }
}


class Solution:
    # if written in java, also 1 ms
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for c in s:
            if c =='(':
                low += 1
                high += 1
            elif c ==')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if high < 0:
                return False
            low = max(0, low)
        return low == 0
#test case: ((*)
#test case: (*)
#test case: (*))
#test case: "(((******))"
#test case: "**((((*)(*((((((((*)((*)"
#test case: "((*)(*))((*"
#test case: "(*()"
# "(*))"



Brute force
class Solution(object):
    def checkValidString(self, s):
        if not s: return True
        A = list(s)
        self.ans = False

        def solve(i):
            if i == len(A):
                self.ans |= valid()
            elif A[i] == '*':
                for c in '() ':
                    A[i] = c
                    solve(i+1)
                    if self.ans: return
                A[i] = '*'
            else:
                solve(i+1)

        def valid():
            bal = 0
            for x in A:
                if x == '(': bal += 1
                if x == ')': bal -= 1
                if bal < 0: break
            return bal == 0

        solve(0)
        return self.ans
"""Time Complexity: O(N * 3^{N})O(N∗3 
N
 ), where NN is the length of the string. For each asterisk we try 3 different values. Thus, we could be checking the validity of up to 3^N3 
N
  strings. Then, each check of validity is O(N)O(N).

Space Complexity: O(N)O(N), the space used by our character array.
"""

