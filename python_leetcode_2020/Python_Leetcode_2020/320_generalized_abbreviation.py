"""
Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

"""

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result=[]
        def dfs(curindex, abbrev, k):
            if curindex == len(word):
                result.append(abbrev + str(k) if k > 0 else abbrev)
                return
                    
            dfs(curindex + 1, abbrev, k + 1)
            dfs(curindex + 1, abbrev + (str(k) if k > 0 else "") + word[curindex], 0)
                
        dfs(0, "", 0)
        return result
