"""
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.

"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count1 = collections.Counter(source)
        count2 = collections.Counter(target)
        count1Set = set(count1.keys())
        for c in target:
            if c not in count1Set:
                return -1
        
        ans = 0
        j = 0
        while j < len(target):
            i = 0 
            while i < len(source) and j < len(target):
                if source[i] == target[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            ans += 1
        return ans
