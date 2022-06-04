"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.
"""

class Solution:
    """
    ["amazon","apple","facebook","google","leetcode"]
    ["lo","eo"]
    Expected: ["google","leetcode"]
        
    ["amazon","apple","facebook","google","leetcode"]
    ["e","o"]
    Expected: ["facebook","google","leetcode"]
    
    ["amazon","apple","facebook","google","leetcode"]
    ["e","oo"]
    ["facebook","google"]
    """
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bchars = collections.defaultdict(int)
        for b in B:
            bcount = collections.Counter(b)
            for key in bcount:
                bchars[key] = max(bchars[key], bcount[key])
        result=[]
        for a in A:
            achars = collections.Counter(a)
            if all(bchars[c] <= achars[c] for c in bchars):
                result.append(a)
        return result
