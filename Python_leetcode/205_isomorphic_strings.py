"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
         Input: "ab"
                "aa"
         Output: true
         Expected: false 
        """
        mapping = {}
        target = set()
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            firstL = s[index]
            secondL = t[index]
            if firstL not in mapping:
                if secondL in target:
                    return False
                target.add(secondL)
                mapping[firstL] = secondL
                
            else:
                if mapping[firstL] != secondL:
                    return False
        return True
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        The main idea is to store the last seen positions of current (i-th) characters in both strings. If previously stored positions are different then we know that the fact they're occuring in the current i-th position simultaneously is a mistake. We could use a map for storing but as we deal with chars which are basically ints and can be used as indices we can do the whole thing with an array.
        """
        sMap = collections.defaultdict(int)
        tMap = collections.defaultdict(int)
        for i in range(len(s)):
            if sMap[s[i]] != tMap[t[i]]:
                return False
            sMap[s[i]] = tMap[t[i]] = i+1
        return True
        
