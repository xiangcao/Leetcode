class Solution:
    # 288 ms
    def validPalindrome(self, s: str) -> bool:
        if not s :
            return True
        def isPalindrom(s):
            return all(s[i] == s[len(s)-i-1] for i in range(len(s)//2 + 1))

        l, r = 0, len(s)-1
        while l < r:
            if s[l].lower() != s[r].lower():
                return isPalindrom(s[:l] + s[l+1:]) or isPalindrom(s[:r] + s[r+1:])
            l += 1
            r -= 1
        return True

#2nd round
    #148 ms
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return isPalindrome(s, start+1, end)
