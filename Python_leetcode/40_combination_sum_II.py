class Solution(object):
    #PASS
    def combinationSum2(self, candidates, target): 
        # write your code here
        candidates.sort()        
        self.ans, curAns, use = [], [], [0] * len(candidates)        
        self.dfs(candidates, target, 0, 0, curAns, use)        
        return self.ans    
    def dfs(self, can, target, p, curSum, curAns, use):        
        if curSum == target:            
            self.ans.append(curAns[:])            
            return        
        for i in range(p, len(can)):            
            if curSum + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):                
                curAns.append(can[i])
                use[i] = 1                
                self.dfs(can, target, i+1, curSum + can[i], curAns, use)                
                curAns.pop()                
                use[i] = 0 
    
    def combinationSum2_(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(index, sum, curanswer, result):
            if sum == target:
                if curanswer not in result: #time limit exceeded. 
                    result.append(curanswer)
                return 
            if sum > target:
                return
            if index < len(candidates):
                dfs(index+1, sum+candidates[index], curanswer+[candidates[index]], result)
                dfs(index+1, sum, curanswer, result)
        candidates.sort()
        index, sum, curanswer, result = 0, 0, [], []
        dfs(index, sum, curanswer, result)
        return result
