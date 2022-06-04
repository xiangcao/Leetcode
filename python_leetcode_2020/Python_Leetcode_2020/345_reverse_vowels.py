class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = list(s)
        l, r = 0, len(s) - 1
        def isVowel(c):
            return c in 'aoeiuAOEIU'
        while l < r:
            while l < r and not isVowel(s[l]):
                l += 1
            while l < r and not isVowel(s[r]):
                r -= 1
            if l < r:
                temp[l], temp[r] = temp[r], temp[l]
                l += 1
                r -= 1
        return ''.join(temp)
