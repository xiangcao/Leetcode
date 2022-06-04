"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]

"""
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        kv = collections.Counter(s)
        mid = [k for k, v in kv.items() if v%2]
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v//2) for k, v in kv.items()])
        half = list(half)
        
        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()
        
        def dfs(start_index):
            if start_index == len(half):
                cur = "".join(half)
                ans.append(cur + mid + cur[::-1])
                return
            for i in range(start_index, len(half)):
                skip = False
                for k in range(start_index, i):
                    if (half[i] == half[k]):
                        skip = True
                        break
                if skip: continue
                half[i], half[start_index] = half[start_index], half[i]
                dfs(start_index+1)
                half[start_index], half[i] = half[i], half[start_index] 
            
        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        # dfs(0)
        return ans
