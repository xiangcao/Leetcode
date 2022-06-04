"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        result = []
        lastPosition = [-1] * 26
        for i, c in enumerate(S):
            lastPosition[ord(c)-ord('a')] = i
        
        start = last = 0
        for i in range(len(S)):
            last = max(last, lastPosition[ord(S[i]) - ord('a')])
            if last == i:
                result.append(last - start + 1)
                start = last + 1
        return result
