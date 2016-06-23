"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Assume that the total area is never beyond the maximum possible value of int.
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        width = min(C,G) - max(A,E)
        height = min(D,H) - max(B,F)
        overlappingArea =  width * height if width > 0 and height > 0 else 0
        
        area1 = (C-A) * (D-B)
        area2 = (G-E) * (H-F)
        
        return area1 + area2 - overlappingArea
