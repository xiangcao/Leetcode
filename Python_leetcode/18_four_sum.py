class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numLen, result, table = len(nums), set(), {}
        if numLen < 4: 
            return []
        nums.sort()
        for i in range(numLen):
            for j in range(i+1, numLen):
                sum = nums[i] + nums[j]
                if not sum in table:
                    table[sum] = [(i, j)]
                else:
                    table[sum].append((i,j))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target - nums[i] - nums[j]
                if T not in table:
                    continue
                else:
                    for k in table[T]:
                        if k[0] > j:
                            result.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in result]
                        
                            
        
