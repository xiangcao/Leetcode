class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        INT_MAX , INT_MIN = (2147483647, -2147483648)
        sum = 0
        l = len(str)
        i = 0 
        neg = False
        while i < l:
            if str[i] == ' ':
                i += 1
            else:
                break
        if i < l:
            if str[i] == '-':
                neg = True
                i = i+1
            if str[i] == '+':
                neg = False
                i = i+1
        while i < l:
            if str[i].isdigit():
                if sum < INT_MAX/10 or (sum == INT_MAX/10 and int(str[i]) <=7) \
                   or (sum == INT_MAX/10 and int(str[i]) ==8 and neg==True):
                    sum = sum*10 + int(str[i])
                    i += 1
                    print sum
                else:
                    return INT_MIN if neg else INT_MAX
            else:
                break
        return sum
            
#solution 2: http://www.cnblogs.com/zuoyuan/p/3777806.html 
s = Solution()

input = raw_input("please input an integer\n")
print s.myAtoi(input)
