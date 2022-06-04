"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""
class Solution(object):
    # Rolling hash
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0
        
        if L > n:
            return -1
        
        a = 26
        modulus = 2 ** 31
        
        haystack_to_int = lambda i : ord(haystack[i]) - ord('a')
        
        needle_to_int = lambda i : ord(needle[i]) - ord('a')
        
        haystack_hash = needle_hash = 0
        for i in range(L):
            needle_hash = (needle_hash * a + needle_to_int(i)) % modulus
            haystack_hash = (haystack_hash * a + haystack_to_int(i)) % modulus
        if haystack_hash == needle_hash:
            return 0
        
        aL = pow(a, L, modulus)
        for start in range(L, n):
            haystack_hash = (haystack_hash * a - haystack_to_int(start-L) * aL + haystack_to_int(start)) % modulus
            
            if haystack_hash == needle_hash:
                return start - L + 1
        return -1
