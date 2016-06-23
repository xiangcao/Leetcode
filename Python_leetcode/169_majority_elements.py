class Solution(object):
    #Accept
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorindex=  0
        count  = 1
        for i in range(1,len(nums)):
            if count == 0:
                majorindex = i
                count = 1
                continue
            if nums[i] == nums[majorindex]:
                count += 1
            else:
                count -= 1
        return nums[majorindex]
      
    #Accept 
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorindex=  0
        count  = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[majorindex]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majorindex = i
                    count = 1
        return nums[majorindex]

    #Accept
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorindex=  0
        count  = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[majorindex]:
                count += 1
            else:
                if count > 0:
                    count -= 1
                elif count == 0:
                    majorindex = i
                    count = 1
        return nums[majorindex]
