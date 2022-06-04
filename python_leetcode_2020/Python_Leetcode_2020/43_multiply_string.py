"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = (ord(num1[i])-ord('0')) * (ord(num2[j]) - ord('0'))
                result[i+j] += product % 10 
                overflow = result[i+j] // 10 
                result[i+j] %= 10
                result[i+j+1] += overflow + product // 10
        # 9133 * 0 = 0000
        while len(result)>1 and result[-1] == 0:
            result.pop()
        return "".join(map(str, result[::-1]))
            
        "0", "0"
        "9", "9"
        "456", "123"
        "999", "999"
