"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=[]
        A = list(a)
        B = list(b)
        carry = 0
        while A or B or carry:
            if A:
                carry += int(A.pop())
            if B:
                carry += int(B.pop())
            result.append(str(carry % 2))
            carry //= 2
        return "".join(result[::-1])

# Round 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2 = len(a)-1, len(b)-1
        carry = 0
        result = []
        while p1 >= 0 or p2 >= 0:
            value1 = int(a[p1]) if p1 >= 0 else 0
            value2 = int(b[p2]) if p2 >= 0 else 0
            value = value1 + value2 + carry
            carry = value // 2
            value = value % 2
            result.append(value)
            p1 -= 1
            p2 -= 1
        if carry > 0:
            result.append(carry)
        
        return "".join(map(str, result[::-1]))

