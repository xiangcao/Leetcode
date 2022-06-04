class Solution:
    def toHex1(self, num: int) -> str:
        if num==0: return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15       # this means num & 1111b
            c = mp[n]          # get the hex char 
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')  #strip leading zeroes
    
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num < 0:
            num += 2 ** 32
        
        stack = []
        s = "0123456789abcdef"
        
        while num:
            stack.append(s[num % 16])
            num //= 16
        
        if not stack:
            return "0"
        
        stack.reverse()
        return "".join(stack)
    
    def toHexBuggy(self, num: int) -> str:
        result = []
        mapping = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6: "6", 7:"7", 8:"8", 9:"9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15:"f"}
        while num:
            remainder = num % 16
            result.append(mapping[remainder])
            if num < 0:
                num = -(-num // 16)
            else:
                num = num // 16
        return "".join(result[::-1])
