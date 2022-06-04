class Solution(object):
    #  Left and Right product lists
    # time O(n). space O(N)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftproduct = [1] * (len(nums))
        rightproduct = [1] * (len(nums))
        for i in range(1, len(nums)):
            leftproduct[i] = leftproduct[i-1] * nums[i-1]
        rightproduct[len(nums)-1] = 1
        
        for j in range(len(nums)-2, -1, -1):
            rightproduct[j] = rightproduct[j+1] * nums[j+1]
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = leftproduct[i] * rightproduct[i]
        return result
    
    # space O(1) (output result array is not considered as space cost)
    def productExceptSelf(self, nums):
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
