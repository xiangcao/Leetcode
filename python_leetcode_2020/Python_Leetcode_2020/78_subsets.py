class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def dfs(subset, cur_index):
            if cur_index == len(nums):
                return result.append(subset)
            # for i in range(cur_index, len(nums)):
            dfs(subset+[nums[cur_index]], cur_index+1)
            dfs(subset, cur_index+1)
        
        dfs([], 0)
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
            
