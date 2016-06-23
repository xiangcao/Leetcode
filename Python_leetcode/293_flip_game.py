class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        pattern=["++", "--"]
        result =[]
        for i in range(len(s)-1):
            flip = list(s)
            for j in range(len(pattern)):
                if s[i:i+2] == pattern[j]:
                    flip[i:i+2] = pattern[1-j]
                    result.append(''.join(flip))
        """
        result =[]
        for i in range(len(s)-1):
            flip = list(s)
            if s[i:i+2] == "++":
                flip[i:i+2] = "--"
                result.append(''.join(flip))
        return result
