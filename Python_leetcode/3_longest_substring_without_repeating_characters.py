class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLen = 0
        hashtable={}
        
        for i in range(len(s)):
            if s[i] in hashtable:
                while start <= hashtable[s[i]]:
                    hashtable.pop(s[start]])
                    start += 1
                maxLen = max(maxLen, i - start + 1)
                hashtable[s[i]] = i
            
        return maxLen   
            
            

            
    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLen = 0 
        hashTable = [-1] * 256
        
        for i in range(len(s)):
            if hashTable[ord(s[i])] != -1:
                while start <= hashTable[ord(s[i])]:
                    hashTable[ord(s[start])] = -1
                    start = start + 1
            if i-start + 1 > maxLen:
                maxLen = i-start + 1
            hashTable[ord(s[i])] = i
        return maxLen

