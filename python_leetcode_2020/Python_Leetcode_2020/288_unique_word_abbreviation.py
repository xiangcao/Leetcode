"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n

Additionally for any string s of size less than or equal to 2 their abbreviation is the same string s.
Find whether its abbreviation is unique in the dictionary. A word's abbreviation is called unique if any of the following conditions is met:

There is no word in dictionary such that their abbreviation is equal to the abbreviation of word.
Else, for all words in dictionary such that their abbreviation is equal to the abbreviation of word those words are equal to word.
"""

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.key_map = {}
        for word in dictionary:
            key = self._getkey(word)
            #If there is more than one string belong to the same key, then the key will be invalid, we set the value to
            if key in self.key_map and self.key_map[key] != word:
                self.key_map[key] = None
            else:
                self.key_map[key] = word

    def isUnique(self, word: str) -> bool:
        key = self._getkey(word)
        return key not in self.key_map or self.key_map.get(key, None) == word
        
    def _getkey(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
