"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        letterToPosition = {letter:index for index, letter in enumerate(order)}
 
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if letterToPosition[w1[j]] > letterToPosition[w2[j]]:
                        return False
                    else:
                        break
            else:
                if len(w1) > len(w2):
                    return False
        return True
            
