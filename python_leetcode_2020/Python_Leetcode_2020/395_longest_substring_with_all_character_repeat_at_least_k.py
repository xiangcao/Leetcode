class Solution(object):
    #O(N) 96 ms
    #test case:  s="a" k=1
    # Sliding Window
    def longestSubstring1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        max_uniq = len(set(s))
        for u in range(1, max_uniq + 1):
            counts = [0] * 26
            left = 0
            right = 0
            unique = 0
            kOrMore = 0
            while(right<len(s)):
                if(unique<=u):
                    idx = ord(s[right])-ord('a')
                    counts[idx] += 1
                    if(counts[idx]==1):
                        unique += 1
                    if(counts[idx]==k):
                        kOrMore += 1
                    right += 1
                else:
                    idx = ord(s[left])-ord('a')
                    counts[idx] -= 1
                    if(counts[idx]==0):
                        unique -= 1
                    if(counts[idx]==k-1):
                        kOrMore -= 1
                    left += 1
                if(unique==u and kOrMore==unique):
                    ans=max(ans,right-left)
        return ans;

    # O(N^2)  6740ms
    # add the countsDict optimization, improved to 360 ms
    def longestSubstring(self, s, k):
        ans = 0
        countsDict = collections.Counter(s)
        
        for i in range(len(s)):
            if countsDict[s[i]] < k:
                continue
            counts = [0] * 26
            uniq = 0
            kOrMore = 0
            for j in range(i, len(s)):
                idx = ord(s[j]) - ord('a')
                counts[idx] += 1
                if counts[idx] == 1:
                    uniq += 1
                if counts[idx] == k:
                    kOrMore += 1                    
                if uniq == kOrMore:
                    ans = max(ans, j - i + 1)
        return ans
                    
# method 3
# worst case o(n^2) Divide and Conquer
Round 2:
    # 32 ms,  faster than 84.61%; Divide and Conquer
    def longestSubstring1(self, s: str, k: int) -> int:
        def longestSubStringUtil(s, start, end, k):
            if end < k: return 0
            countMap = collections.defaultdict(int)
            for i in range(start, end):
                countMap[s[i]] += 1
            for mid in range(start, end):
                if countMap[s[mid]] >= k:
                    continue
                midNext = mid + 1
                while midNext < end and countMap[s[midNext]] < k:
                    midNext += 1
                return max(longestSubStringUtil(s, start, mid, k),
                           longestSubStringUtil(s, midNext, end, k))
            return end - start 
        return longestSubStringUtil(s, 0, len(s), k)
 

    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        max_uniq = len(set(s))
        for u in range(1, max_uniq + 1):
            ans = max(ans, self._longestSubString(s, u, k))
        return ans

    # sliding window using the template in https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
    def _longestSubString(self, s, targetUnique, k):
        count = collections.defaultdict(int)
        start = end = 0
        unique = notlessthanK = 0
        ans = 0
        while end < len(s):
            count[s[end]] += 1
            if count[s[end]] == 1:
                unique += 1
            if count[s[end]] == k:
                notlessthanK += 1
            end += 1
            while unique > targetUnique:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    unique -= 1
                if count[s[start]] == k-1:
                    notlessthanK -= 1
                start += 1
            if unique == targetUnique and unique == notlessthanK:
                ans = max(ans, end-start)
        return ans
