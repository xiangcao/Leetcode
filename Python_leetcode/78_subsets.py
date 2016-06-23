class Solution_wrong(object):
    #Wrong
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 0:
            return []
        for i in range(len(nums)-1, -1, -1):
            subresult = self.subsets(nums[:i])
            for sublist in subresult :
                sublist.append(nums[i])
                result.append(sublist)
                sublist.pop()
                result.append(sublist)
        return result

class Solution(object):
    # pass. but not optimal
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 0:
            return [[]]
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            #subsets(nums[:i])的计算过程本来就已经计算好了subset(nums[:i-1]).
            #所以这里这样循环去计算，就是做了重复计算。每一次i，计算包括了nums[i]的以nums[i]结尾的subset。看下面解法。
            subresult = self.subsets(nums[:i])
            for sublist in subresult:
                result.append(sublist+[nums[i]])
                #result.append(sublist)
            #result.append([])
        result.append([])
        return result

    # pass. 
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 0:
            return [[]]
        nums.sort()
        subresult = self.subsets(nums[:-1])
        for sublist in subresult:
            result.append(sublist+[nums[-1]])
        result.extend(subresult)
        return result

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print "iterative solution"
        result = [[]]
        nums.sort()
        for i in range(len(nums)):
            prevResult = result[:]
            
            for subset in prevResult:
                '''
                won't work. 
                subset.append(nums[i])
                result.append(subset)
                '''
                result.append(subset + [nums[i]]) #pass 
        return result

nums=[1,2]
sol = Solution()
print sol.subsets(nums) 

