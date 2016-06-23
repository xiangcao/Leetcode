class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dict = collections.defaultdict(list)
        for index, w in enumerate(words):
            self.dict[w].append(index)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indxs1 = self.dict[word1]
        indxs2 = self.dict[word2]
        
        i1 = i2 = 0
        mindistance = sys.maxint
        while i1 < len(indxs1) and i2 < len(indxs2):
            mindistance = min(mindistance, abs(indxs1[i1] - indxs2[i2]))
            if indxs1[i1] - indxs2[i2] < 0:
                i1 += 1
            else:
                i2 += 1
        return mindistance
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
