class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0 
        lens = len(nums)
        result = []
        nums.sort()
        while i < lens-2:
            if i != 0 and nums[i] == nums[i-1]: 
                i += 1
                continue
        
            j = i + 1
            k = lens - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k] 
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum < 0:
                    j = j+1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k = k-1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
        return result

    #bug version
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0 
        lens = len(nums)
        result = []
        nums.sort()
        while i < lens-2:
            j = i + 1
            k = lens - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k] 
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sum < 0:
                    j = j+1
                else:
                    k = k-1
            i += 1
        return result
        
nums=[-1,0,1,2,-1,-4]
nums=[-3,14,-10,-1,12,13,-3,2,-6,4,13,7,-8,4,0,-13,11,-4,7,0,4,-3,12,11,5,-14,-8,8,3,-1,-8,-15,-2,-11,-9,-12,9,3,5,-11,-8,3,3,-9,-15,-12,-15,3,-9,0,-12,3,12,-14,-1,-6,-13,-2,-13,-3,12,-14,-3,-13,-9,3,-10,-15,13,2,11,13,-9,-1,11,13,-6,4,1,1,-11,5,-11,8,-2,-5,-12,-8,8,-10,4,-3,-8,-14,-1,-10,-4,-3,12,-14,14,9,6,12,-15,3,10,-13,-8,-11,3,-4,1,-1]
s = Solution()
print s.threeSum(nums)
