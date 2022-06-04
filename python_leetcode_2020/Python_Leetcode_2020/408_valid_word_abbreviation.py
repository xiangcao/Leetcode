"""
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
"""

class Solution(object):
    """
    Test case: "a"   "01"
    Test case: "a"   "2"
    Test case: "internationalization" "i5a11o1"
    Test case "hi" "2i"
    """
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0
        while j < len(abbr) and i < len(word):
            if abbr[j].isalpha():
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                    continue
                else:
                    return False
            start = j
            if abbr[j] == '0':
                return False
            while j < len(abbr) and abbr[j].isdigit():
                j += 1
            
            count = int(abbr[start:j])
            i += count

        return i == len(word) and j == len(abbr)
