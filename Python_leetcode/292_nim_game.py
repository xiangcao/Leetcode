class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #the key is if you can leave the opponent with 4 stones then you win
        return n % 4 != 0
