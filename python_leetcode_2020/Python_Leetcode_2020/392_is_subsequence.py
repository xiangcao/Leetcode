"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

class Solution:
    #Time: O(T) Space: O(1)
    def isSubsequence1(self, s: str, t: str) -> bool:
        sLen, tLen = len(s), len(t)
        
        i = j = 0
        
        while i < sLen and j < tLen:
            if s[i] == t[j]:
                i += 1
            j += 1
 
        return i == sLen
 
    # For the follow up question
    #Time O(|T| + |S|*Log(|T|)); Space:O(|T|)
   # O(T) is for constructing the hashmap which is  one time effort
    def isSubsequence(self, s: str, t: str) -> bool:
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False  # no match at all, early exit

            # greedy match with binary search
            indices_list = letter_indices_table[letter]
            match_index = bisect.bisect_right(indices_list, curr_match_index)
            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False # no suitable match found, early exist

        return True
