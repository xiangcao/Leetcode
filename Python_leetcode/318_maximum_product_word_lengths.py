"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0. 
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        if len(words) <= 1:
            return 0
            
        compressedWord=[0]*len(words) #list of int
        for i in range(len(words)):
            for c in words[i]:
                compressedWord[i] |= (1 << ord(c)-ord('a') )
        maxProduct = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if compressedWord[i] & compressedWord[j] == 0:
                       product = len(words[i]) * len(words[j]) 
                       maxProduct = max(maxProduct, product)
        return maxProduct
            
