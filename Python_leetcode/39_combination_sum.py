from copy import deepcopy

class Solution(object):
     # time limit exceeded 
     def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(index, sum, curanswer, result):
            if sum == target:
                print "sum is %s, curanswer is %s" %(sum, curanswer)
                result.append(curanswer)
                print "result is ", result
                return
            if sum > target or index >= len(candidates):
                return
            print sum, curanswer
            curanswer.append(candidates[index]) 
            dfs(index, sum+candidates[index], deepcopy(curanswer), result)
            curanswer.pop()
            dfs(index+1, sum, curanswer, result)
            
        candidates.sort()
        
        curanswer, result = [], []
        
        dfs(0, 0, curanswer, result)
        print "final result ", result 
        return result



#Solution 2: PASS http://www.cnblogs.com/zuoyuan/p/3777540.html
class Solution2:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret

candidates=[1,2,3]
target = 7

candidates=[41,21,30,32,38,22,39,31,36,48,44,35,43,34,45,20,26,25,24,40,33,23,46,29,42,37,28,49,27]
target = 64

candidates=[1,1]
target=1

s = Solution2()
print s.combinationSum(candidates, target)

