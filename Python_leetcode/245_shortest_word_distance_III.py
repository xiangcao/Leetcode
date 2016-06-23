class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = index2 = -1
        mindistance = len(words)
        for index, w in enumerate(words):
            if w == word1 or w == word2:
                if word1 == word2:
                    index1, index2 = index2, index
                elif w == word1:
                    index1 = index
                else:
                    index2 = index
                if index1 == -1 or index2 == -1:
                    continue
                else:
                    mindistance = min( abs(index1-index2), mindistance)
        return mindistance
        
