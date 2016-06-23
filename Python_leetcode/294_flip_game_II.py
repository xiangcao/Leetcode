class Solution(object):
    canWinTable={}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # "+++++" -> cannot guarantee  
        # "+++" -> can win
        # the key is to find the maximum number of consecutive + in the string. if larger than 4, then cannot guarantee win
        # if <= 4 but >=2 then can guarantee win
        if s in self.canWinTable:
            return self.canWinTable[s]
        nextStates = self.generatePossibleNextMoves(s)
        for state in nextStates:
            if not self.canWin(state):
                self.canWinTable[s]=True
                return True
        self.canWinTable[s] = False
        return False
                 
        
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result =[]
        for i in range(len(s)-1):
            flip = list(s)
            if s[i:i+2] == "++":
                flip[i:i+2] = "--"
                result.append(''.join(flip))
        return result
