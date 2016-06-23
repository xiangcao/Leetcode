class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 10/3= 3.3 more than 3.3 is 4. at most 2 such number
        # n/3, at most 2 such number
        
        n1, n2, c1, c2 = None, None, 0, 0
        result = []
        for i in nums:
            if i == n1:
                c1 += 1
            elif i == n2:
                c2 +=1
            elif c1 > 0 and c2 > 0:
                c1 -= 1
                c2 -= 1
            else:
                if c1 == 0:
                    c1 = 1
                    n1 = i
                else:
                    c2 = 1
                    n2 = i
        c1 = c2 = 0
        for i in nums:
            if i == n1:
                c1 += 1
            elif i == n2:
                c2 += 1
        if c1 > len(nums)/3:
            result.append(n1)
        if c2 > len(nums)/3:
            result.append(n2)
        return result
            
       
# C++ solution for generalized major element with count > n/k
#https://leetcode.com/discuss/95467/share-my-solution-for-generalized-major-element-with-count
 
