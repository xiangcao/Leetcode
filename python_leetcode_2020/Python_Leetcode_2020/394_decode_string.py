"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
"""

class Solution(object):
    # accepted. my own solution. not clean;
    def decodeString1(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        i = 0
        stack=[]
        while i < size:
            repeat = 0
            if s[i] == ']':
                decodedString = ""
                while stack and not stack[-1].isdigit():
                    decodedString = stack.pop() + decodedString
                if stack[-1].isdigit():
                    stack.append(decodedString * int(stack.pop()))
                else:
                    stack.append(decodedString)
                i += 1
                continue

            while s[i].isdigit():
                repeat = repeat * 10 + int(s[i])
                i += 1
            if repeat != 0 :
                stack.append(str(repeat))
 
            if s[i] == '[':
                j = i + 1
                while s[i] != ']' and not s[i].isdigit():
                    i += 1
                stack.append(s[j:i])
            else:
                stack.append(s[i])
                i += 1

        return "".join(stack)


    # better. more clean
    # keep appending to stack until we see `]`; then start the decoding process
    def decodeString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        i = 0 
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                decodedString = ""
                while stack[-1] != '[':
                    decodedString = stack.pop() + decodedString
                stack.pop()
                
                repeat = 0
                base = 1
                while stack and stack[-1].isdigit():
                    repeat = repeat + base * int(stack.pop())
                    base *= 10
                
                stack.append(repeat * decodedString)
        return "".join(stack)
    
    # Also very clean; using the same processing order as my first solution but is much more logical and clean
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

# recursion in python
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.pos = 0
        self.s = s
        return self._decode()
    def _decode(self):
        num = 0
        word = ""
        while self.pos < len(self.s):
            cur = self.s[self.pos]
            if cur == '[':
                self.pos += 1
                curstring = self._decode()
                word += curstring * num
                num = 0
            elif cur.isdigit():
                num = num * 10 + int(cur)
            elif cur == ']':
                return word
            else:
                word += cur
            self.pos += 1
        return word                
           
# Recursion
class Solution {
public:
    string decodeString(string s) {
        int pos = 0;
        return helper(pos, s);
    }
    
    string helper(int& pos, string s) {
        int num=0;
        string word = "";
        for(;pos<s.size(); pos++) {
            char cur = s[pos];
            if(cur == '[') {
                string curStr = helper(++pos, s);
                for(;num>0;num--) word += curStr;
            } else if (cur >= '0' && cur <='9') {
                num = num*10 + cur - '0';
            } else if (cur == ']') {
                return word;
            } else {    // Normal characters
                word += cur;
            }
        }
        return word;
    }
}; 
