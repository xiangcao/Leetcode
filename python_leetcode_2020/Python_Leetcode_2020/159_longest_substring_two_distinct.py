class Solution(object):
    #1: 56ms;  #2: 84ms; #3: 40ms
    def lengthOfLongestSubstringTwoDistinct1(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        count = collections.Counter()
        maxLen = 0
        while r < len(s):
            count[s[r]] += 1
            r += 1
            if len(count) > 2:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            else:
                maxLen = max(maxLen, r - l)
        return maxLen

    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        count = collections.Counter()
        while r < len(s):
            count[s[r]] += 1
            r += 1
            if len(count) > 2:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
        return len(s) - l

    # following the 10 line template described in leetcode 76 most voted solution
    def lengthOfLongestSubstringTwoDistinct2(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        count = collections.Counter()
        maxLen = 0
        while r < len(s):
            count[s[r]] += 1
            r += 1
            
            while len(count) > 2:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1

            maxLen = max(maxLen, r - l)

        return maxLen
    
    def lengthOfLongestSubstringTwoDistinct3(self, s):
        n = len(s) 
        if n < 3:
            return n
        
        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position 
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2
        
        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len
