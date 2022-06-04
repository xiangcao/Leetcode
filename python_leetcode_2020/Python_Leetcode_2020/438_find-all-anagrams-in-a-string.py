from typing import List
import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        
        target_count = collections.Counter(p)
        sliding_count = collections.Counter(s[:window])
        index = window - 1
        result = []
        while index < len(s):
            if sliding_count == target_count:
                result.append(index-window+1)
            sliding_count[s[index-window+1]] -= 1
            if sliding_count[s[index-window+1]] == 0:
                del sliding_count[s[index-window+1]]
            index += 1
            if (index < len(s)):
                sliding_count[s[index]] += 1

        return result

x = Solution()
s = "cbaebabacd"
p = "abc"
x.findAnagrams(s, p)

# round 2
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        targetcount = collections.Counter(p)
        slidingcount = collections.Counter(s[:window-1])
        result = []
        index = window-1
        while index < len(s):
            slidingcount[s[index]] += 1
            index += 1
            if slidingcount == targetcount:
                result.append(index-window)
            
            slidingcount[s[index-window]] -= 1
            # this line is important because those irrelevant characters are added into the map
            if slidingcount[s[index-window]] == 0:
                slidingcount.pop(s[index-window])
        return result
            

# round 3
class Solution:
    """ first buggy version
    Input: "abab"  "ab"
    Output:  [0,1]
    Expected: [0,1,2]
    
    need one more check after the loop
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen = len(p)
        target = collections.Counter(p)
        window = collections.Counter(s[:plen])
        result = []
        for i in range(plen,len(s)):
            if window == target:
                result.append(i-plen)
            window[s[i-plen]] -= 1
            window[s[i]] += 1
            if window[s[i-plen]] == 0:
                window.pop(s[i-plen])
        return result
            
    # s: "abab",  p: "ab"
    # s: "cbacebabacd";  p:"abc"
    # s "cbaebabacd"  p "abc";  
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen = len(p)
        target = collections.Counter(p)
        window = collections.Counter(s[:plen-1])
        result = []
        for i in range(plen-1,len(s)):
            window[s[i]] += 1
            if i >= plen:
                window[s[i-plen]] -= 1
                if window[s[i-plen]] == 0:
                    window.pop(s[i-plen])  # key error? 
            if window == target:
                result.append(i-plen+1)
        return result
            
