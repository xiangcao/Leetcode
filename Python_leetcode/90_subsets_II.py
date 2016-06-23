#Subsets II


class Solution(object):
    level =  0
    def subsetsWithDup_(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #how many possibilities
        # n = len(nums)
        #if no duplicate 2^n 
        #assume k identical number, 2^(n-k) * (k+1). the reason is for the k identical number, we have k+1 possiblities (0 occurence, 1 occurence, 2 occurence, ...., k occurence). for all other n-k unique numbers, we still have 2 possibilties for each of them
        #[1,2]=  => [1 2] [2] + [1] []
        #[1,2,2] =>   [1,2,2] [2,2] .+  [1,2] [2] [1] []
        #[1,2,3] => [1,2,3] [2,3] [1,3] [3] [1,2] [2] [1] []
        #[1,2,2,2] = >[1,2,2,2],[2,2,2] +  [1 2 2] [2 2] [1 2] [2] [1] []
        if len(nums) == 0:
            return [[]]
        nums.sort()
        result = []
        Solution.level += 1
        subresults = self.subsetsWithDup(nums[:-1])
        for index, item in enumerate(subresults):
            if  item == None:
                subresults.remove(item)
                break
            result.append(item + [nums[-1]])
        print Solution.level, result 
        if Solution.level != 1:
            result.append(None)
        result.extend(subresults)
        print Solution.level, result
        Solution.level -= 1
        return result

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """  
        result = []
        nums.sort()
        def helper(curpos, cursubset):
            result.append(cursubset)
            for i in range(curpos, len(nums)):
                if i != curpos and nums[i] == nums[i-1]: continue
                helper(i+1, cursubset+[nums[i]])
        helper(0, [])
        return result

    #iterative solution
                        
nums=[1,2,3,4,5,6,7,8,10,0]

sol = Solution()

sol.subsetsWithDup(nums) 
