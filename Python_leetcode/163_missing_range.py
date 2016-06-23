class Solution(object):
    #ACCEPTED
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result=[]
        if len(nums) == 0:
            leftRange, rightRange = lower, upper
            if leftRange == rightRange:
                result.append(str(leftRange))
            elif leftRange < rightRange:
                result.append(str(leftRange)+"->"+str(rightRange))
            return result
        index = 0
       
        leftRange, rightRange = lower, nums[0]-1
        for k in range(1, len(nums)+2):
            if leftRange == rightRange:
                result.append(str(leftRange))
            elif leftRange < rightRange:
                result.append(str(leftRange)+"->"+str(rightRange))
            if k == len(nums): 
                leftRange, rightRange = nums[-1]+1, upper
            elif k < len(nums):
                leftRange, rightRange = rightRange+2, nums[k]-1
        return result
    #compare with someone else's code https://segmentfault.com/a/1190000003790309 



    #time limit exceeded
    def findMissingRanges_(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result=[]
        index = 0
        import pdb
#        pdb.set_trace()
        def range(begin, stop):
            i = begin
            while i < stop:
                yield i
                i += 1
        leftRange, rightRange = None, None
        for k in range(lower, upper+1):
            if index >= len(nums):
                return result
            print " k is %s, nums[index] is %s" %(k, nums[index])
            if k == nums[index]:
                if leftRange:
                    print "find a right bound"
                    rightRange = k - 1
                    result.append(str(leftRange)+"->"+str(rightRange))
                    leftRange, rightRange = None, None
                index += 1
            elif k != nums[index] and not leftRange:
                leftRange = k
            
        if leftRange and not rightRange:
            result.append(str(leftRange)+"->"+str(upper))
        return result
                
                
sol = Solution()
nums=[-1000000000,-9999,0,1,2,10,100,1000,999999999,1000000000]
lower= -1000000000
upper = 1000000000

nums=[0,1,3,50,75]
lower=0
upper=99

result = sol.findMissingRanges(nums, lower, upper) 
print result

"""
 Time Limit Exceeded
Last executed input: [-1000000000,-9999,0,1,2,10,100,1000,999999999,1000000000]
-1000000000
1000000000 
['-999999999->-10000', '-9998->-1', '3->9', '11->99', '101->999', '1001->999999998']
"""
