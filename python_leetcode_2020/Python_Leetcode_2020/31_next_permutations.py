class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums)-1
        while right > 0:
            if nums[right] > nums[right-1]:
                break
            right -= 1
        k = len(nums)-1
        if right > 0:
            while k >= right:
                if nums[k] > nums[right-1]:
                    nums[k], nums[right-1] = nums[right-1], nums[k]
                    break
                k -= 1
        i = right
        j = len(nums)-1
        while i < j :
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
                
