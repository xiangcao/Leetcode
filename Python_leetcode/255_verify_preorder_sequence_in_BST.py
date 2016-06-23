#https://leetcode.com/discuss/51543/java-o-n-and-o-1-extra-space

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        return self._verifyPreorder(preorder,0, len(preorder)-1)
    # Brute force, recursive solution. O(n^2) time

    def _verifyPreorder(self, preorder, begin, end):
        if begin >= end:
            return True
        root = preorder[begin]
        rightchildroot = begin + 1
        while rightchildroot <= end and preorder[rightchildroot] < root:
            rightchildroot += 1
        right = rightchildroot
        while right <= end:
            if preorder[right] > root:
                right += 1
            else:
                return False
               
        return self._verifyPreorder(preorder, begin+1, rightchildroot-1) and \
               self._verifyPreorder(preorder, rightchildroot, end)
        
    #O(n) time, O(h) space 
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack=[]
        low = float("-inf")
        
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()      #low is increasing in this iteration
            stack.append(p)
        return True
        
    #O(n) time, o(1) space
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = float("-inf")
        stack = -1
        
        for p in preorder:
            if p < low:
                return False
            while stack >= 0 and p > preorder[stack]:
                low = preorder[stack]
                stack -= 1
            stack += 1
            preorder[stack] = p
        return True
        
