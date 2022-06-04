"""Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
 

Constraints:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
0 <= i <= j <= nums.length - 1
"""

class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = self.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.buildTree(nums, 0, len(nums)-1)

    def buildTree(self, nums, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            root.sum = nums[start]
            return root
        mid = start + (end-start) // 2
        root.left = self.buildTree(nums, start, mid)
        root.right = self.buildTree(nums, mid+1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        def _updateHelper(node, i, val):
            if node.start == node.end:
                node.sum = val
                return
            mid = node.start + (node.end-node.start) // 2
            if i <= mid:
                 _updateHelper(node.left, i, val)
            else:
                _updateHelper(node.right, i, val)
            node.sum = node.left.sum + node.right.sum
        _updateHelper(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def _sumRange(node, i, j):
            if node.end == j and node.start == i:
                return node.sum
            mid = node.start + (node.end-node.start) // 2
            if j <= mid:
                return _sumRange(node.left, i, j)
            elif i > mid:
                return _sumRange(node.right, i, j)
            else:
                return _sumRange(node.left, i, mid) + _sumRange(node.right, mid+1, j)
        return _sumRange(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
