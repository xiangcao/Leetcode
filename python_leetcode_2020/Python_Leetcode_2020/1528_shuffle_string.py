"""Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"
"""
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # cyclic sort
        def swap(array, i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        s = list(s)
        for i in range(len(indices)):
            while(indices[i]!=i):
                swap(s, i,indices[i])
                swap(indices, i,indices[i])
        return "".join(s)
