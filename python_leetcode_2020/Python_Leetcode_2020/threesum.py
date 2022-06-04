class Solution(object):
    @classmethod
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort();
        results = []
        for i in range(len(nums)-2):
            jj = i + 1
            k = len(nums)-1
            while jj < k:
                total = nums[i] + nums[jj] + nums[k]
                if total == 0:
                    results.append([i, jj, k])
                    jj += 1
                    import pdb
                    pdb.set_trace()
                    while jj < k and nums[jj] == nums[jj-1]:
                        jj += 1
                    k -= 1
                elif total < 0 : 
                    jj += 1
                else:
                    k -= 1
        return results
nums=[-1,0,1,2,-1,-4]
result = Solution.threeSum(nums)
print(result)
