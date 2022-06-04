class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(None)
        def dfs(index):
            if index == len(s):
                return 1
            count = 0
            if 9 >= int(s[index]) >= 1:
                count += dfs(index+1)
            if 26 >= int(s[index:index+2]) >= 10:
                count += dfs(index+2)
            return count
        return dfs(0)
                
