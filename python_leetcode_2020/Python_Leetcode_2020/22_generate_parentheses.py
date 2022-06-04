class Solution:
    # 24 ms
    #backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        
        def generate(current, left, right):
            if (right == n):
                result.append(current)
                return
            
            if left < n:
                generate(current + '(', left + 1, right)
            if right < left:
                generate(current + ')', left, right + 1)
        generate("", 0, 0)
        return result
    
    # 124 ms
    #brute force
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
