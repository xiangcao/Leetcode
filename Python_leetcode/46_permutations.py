class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def permutehelper(index):
            if index == len(nums):
                result.append(copy.deepcopy(nums))
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permutehelper(index+1)
                nums[i], nums[index] = nums[index], nums[i] # line 15
            
        permutehelper(0)
        return result

    # fix every element at the last position, 
    # then get the full permuation of the remainig n-1 elements 
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for perm in self.permute(nums[:i]+ nums[i+1:]):
                res.append(perm + [nums[i]])
        return res

    #插入法        
    def permute(self, num):
        if len(num) < 2:
            return [num]
        ret = []
        for permu in self.permute(num[:-1]):
            ret += [permu[:i] + [num[-1]] + permu[i:] for i in range(len(permu) + 1)]
        return ret


'''
without line 15, it will fail. 

Input: [1,2,3]
Output: [[1,2,3],[1,3,2],[3,1,2],[3,2,1],[1,2,3],[1,3,2]]
Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 

'''
