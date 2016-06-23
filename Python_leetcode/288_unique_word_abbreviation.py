class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = collections.defaultdict(set)
        for word in dictionary:
            if len(word)>2:
                abbrev = word[0] + str(len(word)-2) + word[-1]
            else:
                abbrev = word
            self.dict[abbrev].add(word)
    
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) > 2:
            abbrev = word[0] + str(len(word)-2) + word[-1]
        else:
            abbrev = word
        print abbrev
        
        if abbrev not in self.dict or (len(self.dict[abbrev]) == 1 and list(self.dict[abbrev])[0] == word):
            return True
        else:
            return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
