class Solution:
    # 64 ms;
    # HashMap Time: Average O(N^2), Worst O(N^4) when all elements are duplicates
    # space O(N^2)
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        numLen, result, table = len(nums), set(), {}
        if numLen < 4: 
            return []
        nums.sort()
        if target < nums[0]*4 or target > nums[-1]*4:  # early termination
            return

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

    # 428 ms; Time O(N^3); Space: 
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort() 
        results = []
        if target < nums[0]*4 or target > nums[-1]*4:  # early termination
            return
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                p = j + 1
                q = len(nums)-1
                while p < q:
                    s = nums[i] + nums[j] + nums[p] + nums[q]
                    if s > target or (q < len(nums)-1 and nums[q] == nums[q+1]):
                        q -= 1
                    elif s < target or ( p > j + 1 and nums[p] == nums[p-1]):
                        p += 1
                    else:
                        results.append((nums[i], nums[j], nums[p], nums[q]))
                        p += 1
                        q -= 1
        return results

    # 84 ms
    # Time O(N^3); Space O(1)
    def fourSum3(self, nums: List[int], target: int) -> List[List[int]]:
                    
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
