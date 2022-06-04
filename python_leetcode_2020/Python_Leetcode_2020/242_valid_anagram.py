"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = collections.defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1
        
        return all(x == 0 for x in counter.values())

Follow up

What if the inputs contain unicode characters? How would you adapt your solution to such case?

Answer

Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.



