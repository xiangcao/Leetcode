#Input: "bbbba"
#".*a*a"
#Output: false
#Expected: true 

#s="a"
#p="ab*"


'''
 Input: "bbbba"
".*a*a"
Output: false
Expected: true 

'''
class Solution(object):
    #time limit exceeded
    #"aaaaaaaaaaaaab"
    #"a*a*a*a*a*a*a*a*a*a*c"
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def isMatchHelper(sIndex, pIndex):
            if pIndex == len(p):
                if sIndex == len(s):
                    return True
                else:
                    return False
            if p[pIndex] == '*':
                return isMatchHelper(sIndex, pIndex+1) or \
                       isMatchHelper(sIndex, pIndex-1) or \
                       isMatchHelper(sIndex-1, pIndex+1)

            if sIndex ==  len(s):
                return pIndex == len(p) or (pIndex == len(p)-2 and p[pIndex+1] == '*')
            
            if p[pIndex] ==  '.' or p[pIndex] == s[sIndex]:
                return isMatchHelper(sIndex+1, pIndex+1)
            #elif(pIndex < len(p)-1 and p[pIndex + 1] == '*'): # s: "a", "b*"
            #    return isMatchHelper(sIndex, pIndex + 2)
            else:
                return False

        return isMatchHelper(0,0)


sol = Solution()
s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"
s="hello"
p="hel*o"
s="a"
p="a*"
print sol.isMatch(s,p)

