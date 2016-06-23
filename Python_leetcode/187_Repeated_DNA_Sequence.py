class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mapping = {'A':0, 'C':1, 'G':2, 'T':3}
        base = len(mapping)
        base_power_9 = pow(base, 9)
        
        rollinghash= set()
        result =set()
        
        rhash = 0 
        for index in range(len(s)):
            if index > 9:
                rhash -= mapping[s[index-10]] * base_power_9
            rhash = rhash * base + mapping[s[index]]
            if index > 8:
                if rhash in rollinghash:
                    result.add(s[index-9: index+1])
                else:
                    rollinghash.add(rhash)
        return [s for s in result]
       

# I borrowed the idea in this post: https://leetcode.com/discuss/24595/short-java-rolling-hash-solution

# another amazing solution: https://leetcode.com/discuss/24478/i-did-it-in-10-lines-of-c

# learn about rolling hash: http://courses.csail.mit.edu/6.006/spring11/rec/rec06.pdf
 
