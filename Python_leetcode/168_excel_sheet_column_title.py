class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        
        while n:
            offset = n % 26
            if offset == 0:
                offset = 26
            result += chr(ord('A') -1 + offset)
            n /= 26
            if offset == 26:
                n -= 1
        return result[::-1]

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        
        while n:
            n -= 1
            offset = n % 26
            result.append(chr(ord('A') + offset))
            n /= 26
        return ''.join(result[::-1])


    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))
