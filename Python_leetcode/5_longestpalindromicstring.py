class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLen = len(s)
        table = [[0 for x in range(strLen)] for y in range(strLen)]
        
        for x in range(strLen):
            table[x][x] = 1
            maxLen = 1
        result= s[0]
        length = 2
        while length <= strLen:
            i = 0
            while i < strLen - length + 1:
                j = i + length - 1  # j < strLen
                if s[i] == s[j]:
                    if i+1 > j-1 or table[i+1][j-1]:
                        table[i][j] = 1
                        if j-i+1 > maxLen:
                            maxLen = j-i+1
                            result = s[i:j+1]
                    else:
                        table[i][j] = 0
                else:
                    table[i][j] = 0

                i += 1
                
            length += 1
        return result 


    #wrong solution
    def longestPalindrome_2(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLen = len(s)
        table = [[0 for x in range(strLen)] for y in range(strLen)]
        
        for x in range(strLen):
            table[x][x] = 1
            maxLen = 1
        result= s[0]
        i = 0 
        while i < strLen-1:
            j = i + 1
            while j < strLen:
                
                if s[i] == s[j]:
                    if i+1 > j-1 or table[i+1][j-1]:
                        table[i][j] = 1
                        if j-i+1 > maxLen:
                            maxLen = j-i+1
                            result = s[i:j+1]
                    else:
                        table[i][j] = 0
                else:
                    table[i][j] = 0

                j += 1
                
            i += 1
        return result
                    
            
                        
        
input = raw_input("please input a string\n")
s = Solution()
print s.longestPalindrome(input)
