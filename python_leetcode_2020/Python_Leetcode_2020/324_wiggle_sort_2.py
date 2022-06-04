class Solution:
    # sort; nlogn
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = sorted(nums)
        n = len(nums)
        m = (n+1) >> 1
        j = 0
        for i in range(m-1, -1, -1):
            nums[j] = copy[i]
            j += 2
        j = 1
        for i in range(n-1, m-1, -1):
            nums[j] = copy[i]
            j += 2

    # https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference
    # use 3 way partitioning;  O(n)
