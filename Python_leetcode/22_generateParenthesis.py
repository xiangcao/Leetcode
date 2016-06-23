class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        s=''
        self.dfs(s, n, n, result)
        return result
    def dfs(self, s, left, right, result):
        if left > right:
            return
        if left == 0 and right == 0:
            result.append(s)
            return
        if left >  0:
            self.dfs(s+'(', left-1, right, result)
        if right > 0:
            self.dfs(s+')', left, right-1, result)
        
