class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result=[]
        self.dfs(word, 0, 0, '', result)
        return result
        
    def dfs(self, word, index, count, answer, result):
        if index==len(word):
            if count:
                answer += str(count)
            result.append(answer)
            return
        #abbreviate
        self.dfs(word, index+1, count+1, answer, result)
        #not abbreviate
        if count:
            answer+=str(count)
        answer += word[index]
        self.dfs(word, index+1, 0, answer, result)
        
    #BUGGY     
    def dfs2(self, word, index, result):
        if index == len(word):
            result.append(word)
            return
        self.dfs(word, index+1, result)
       
        
        if word[index-1].isdigit():
            word2 = word[:index-1]+ str(int(word[index-1])+1) + word[index+1:]
            #when word[index-1] == '9'
            self.dfs(word2, index, result)
        else:
            word1 = word[:index]+'1'+word[index+1:]
            self.dfs(word1, index+1, result)
       


input=raw_input("please input a string\n")
s = Solution()
result = s.generateAbbreviations(input)
print result
