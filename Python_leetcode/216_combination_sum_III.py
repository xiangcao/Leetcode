class Solution(object):
    #accpeted
    def combinationSum3(self, k, n):
        ans = []
        def search(start, cnt, sums, nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                ans.append(nums)
                return
            for x in range(start + 1, 10):
                search(x, cnt + 1, sums + x, nums + [x])
        search(0, 0, 0, [])
        return ans
    #accpted 
    def combinationSum3_(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(index, sum, count, curanswer):
            if sum == n and count == k and index <= 10:
                #if curanswer not in result: #time limit exceeded.
                result.append(curanswer)
                return
            if sum > n or count > k or index >10:
                return
            if index < 10:
                dfs(index+1, sum+index, count+1, curanswer+[index])
                dfs(index+1, sum, count, curanswer)
        index, sum, count, curanswer, result = 1, 0, 0, [], []
        dfs(index, sum, count, curanswer)
        return result
