class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxpower = math.pow(3, int(math.log(0xffffffff)/math.log(3)))
        return n > 0 and maxpower % n == 0
        
        #
        return n>0 and math.pow(3, int(math.log(3,n))) == n
        
        return n>0 and math.pow(3, round(math.log(3,n))) == n
       

#http://blog.csdn.net/ebowtang/article/details/50485622
#http://bookshadow.com/weblog/2016/01/08/leetcode-power-three/ 
