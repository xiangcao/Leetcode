class Solution(object):
    
    """
Input: 12345
Output: "TwelveThousand Three Hundred Fourty Five"
Expected: "Twelve Thousand Three Hundred Forty Five"

Input: 1000010
Output: "One Million  Ten"
Expected: "One Million Ten
    
    
Input: 1000000
Output: "One Million  Thousand"
Expected: "One Million"


Input: 1000
Output: "One Thousand "
Expected: "One Thousand"



Input: 0
Output: ""
Expected: "Zero"

Input: 100000
Output: "One Hundred  Thousand"
Expected: "One Hundred Thousand" 

"""
# this solution is almost same to mine: https://leetcode.com/discuss/55462/my-clean-java-solution-very-easy-to-understand
# suggested for interview!!! https://leetcode.com/discuss/71544/short-clean-java-solution 
# stephan's simple solution in python: https://leetcode.com/discuss/55477/recursive-python
# https://leetcode.com/discuss/57747/fairly-clear-4ms-c-solution

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        mappingSmaller=[["", "One","Two", "Three","Four","Five","Six","Seven","Eight","Nine"],["Ten", "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"],"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        mappingLarger=["","Thousand", "Million", "Billion"]
        
        def convertToEnglish(num):
            result = ""
            curSegment = ""
            if not num:
                return result
            if num/100:
                result += mappingSmaller[0][num/100]+ " Hundred "
                result += convertToEnglish(num%100) 
            elif num/10 == 0:
                result += mappingSmaller[0][num] +" "
            elif num/10 == 1:
                result += mappingSmaller[1][num%10]+" "
            else:
                result += mappingSmaller[num/10] + " " + convertToEnglish(num%10)
            return result
        
        curGroup = 0
        words = ""
        while num:
            chunkNumber = num % 1000 
            chunckEnglish = convertToEnglish(chunkNumber)
            if chunckEnglish: 
                words = chunckEnglish + mappingLarger[curGroup] +" " +words
            num = num / 1000
            curGroup += 1
            
        return words.strip()



    #solution 2 Accepted. my first solution
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        mappingSmaller=[["", "One","Two", "Three","Four","Five","Six","Seven","Eight","Nine"],["Ten", "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"],"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        mappingLarger=["Thousand", "Million", "Billion"]
        
        def convertToEnglish(num):
            result = ""
            curSegment = ""
            if num/100:
                result += mappingSmaller[0][num/100]+ " Hundred "
                num = num%100
            if num/10 == 0:
                result += mappingSmaller[0][num]
            elif num/10 == 1:
                result += mappingSmaller[1][num%10]
            else:
                result += mappingSmaller[num/10] + " " + mappingSmaller[0][num%10]
            return result.strip()
            
            
        
        curGroup = - 1
        words = []
        while num:
            chunkNumber = num % 1000 
            chunckEnglish = convertToEnglish(chunkNumber)
            if chunckEnglish:   #without this check, we get ["Ten", "", "One Million"] https://leetcode.com/submissions/detail/64017793/
                words.append(chunckEnglish)
            if curGroup>=0 and chunkNumber>0:
                words[-1] += " " +mappingLarger[curGroup]
            print words, num
            num = num / 1000
            curGroup += 1
            
        return " ".join(words[::-1]).strip()
