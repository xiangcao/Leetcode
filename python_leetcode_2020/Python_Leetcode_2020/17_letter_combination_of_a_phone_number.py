"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3':'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result=[]
        if not digits:
            return []
        subresults= self.letterCombinations(digits[1:])

        for l in mapping[digits[0]]:
            if not subresults:
                result.append(l)
                continue
            for sub in subresults:
                result.append(l + sub)
        return result
        
