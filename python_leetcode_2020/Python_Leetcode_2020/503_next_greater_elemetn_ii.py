class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:  
        n = len(nums)
        result = [-1] * n
        stack = [] # index stack
        #count = 0
        for i in range(2*n):
            num = nums[i % n] 
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
                #count += 1
            if (i < n): stack.append(i)
            #if count == n:
            #    break
        return result
    
        """ 
        use solution for Next Greater Elements I. 

        this solution only works if there are no duplicates in nums
        nums1 = nums
        nums2 = nums + nums
        mapToGreater={}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                mapToGreater[stack.pop()] = num
            stack.append(num)
        result = []
        for num in nums1:
            result.append(mapToGreater.get(num, -1))
        return result
    """
