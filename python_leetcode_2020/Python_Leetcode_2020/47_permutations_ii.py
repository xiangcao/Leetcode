class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def dfs(start_index):
            if start_index == len(nums)-1:
                result.append(list(nums))
                return
            for i in range(start_index, len(nums)):
                skip = False
                for k in range(start_index, i):
                    if (nums[i] == nums[k]):
                        skip = True
                        break
                if skip: continue
                nums[i], nums[start_index] = nums[start_index], nums[i]
                dfs(start_index+1)
                nums[start_index], nums[i] = nums[i], nums[start_index]
        dfs(0)
        return result

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        def dfs(nums, l):
            if l == n-1:
                res.append(list(nums))
                return 
            for i in set(nums[l:]):
                remaining = nums[l:]
                remaining.remove(i)
                dfs(nums[:l] + [i] + remaining, l+1)
        dfs(nums, 0)
        return res

    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

sol = Solution()
# nums = [-1,2,0,-1,1,0,1]
nums = [2,2,1,1]
print(len(sol.permuteUnique1(nums)))
