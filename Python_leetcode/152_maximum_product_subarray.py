class Solution(object):
    def maxProduct_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #testcase [-2]
        maxProduct = min(nums)
        maxPosProduct = 1
        minNegProduct = 1
        for i in nums:
            if i > 0 :
                maxPosProduct = max(maxPosProduct * i, i)
                minNegProduct  = min(minNegProduct * i, i)
            else:
                prevMinNegProduct = minNegProduct
                minNegProduct = min (maxPosProduct * i, i)
                maxPosProduct = max (prevMinNegProduct * i, i)
            maxProduct = max(maxProduct, maxPosProduct)

        return maxProduct
        
        
    def maxProduct(self, nums):
        minNegProduct, maxPosProduct, maxProduct = 1, 1, min(nums)
        for i in nums:
            newMinNegProduct = min (minNegProduct * i, maxPosProduct * i, i )
            maxPosProduct = max(i, maxPosProduct * i, minNegProduct * i)
            minNegProduct = newMinNegProduct
            maxProduct = max(maxProduct, maxPosProduct)
        return maxProduct
        
