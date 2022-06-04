class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0 
        rangesum = [0]
        movingsum = 0
        """
        for e in nums:
            movingsum += e
            rangesum.append(movingsum)

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (rangesum[j+1] - rangesum[i] == k):
                # if ( sum(nums[i:j+1]) == k) :
                    count+=1
        """
        counter = collections.Counter()
        counter[0] = 1
        
        presum = 0
        totalCount = 0
        for e in nums:
            presum += e
            totalCount += counter[presum - k]
            counter[presum] += 1

        return totalCount
                

                
        
        
