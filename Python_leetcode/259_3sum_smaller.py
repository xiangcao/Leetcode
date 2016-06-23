class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        numSolution = 0
        for i in range(length-2):
            j, k=i+1, length-1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    numSolution += k-j
                    j += 1
                    k = length -1
                    
                else:
                    k -= 1
        return numSolution
