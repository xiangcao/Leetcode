class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        exist=set()
        for i in s:
            if i in exist:
                exist.remove(i)
            else:
                exist.add(i)
        return True if len(exist) <= 1 else False
