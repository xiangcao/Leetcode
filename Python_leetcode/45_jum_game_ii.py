class Solution(object):
    #pass
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        i, maxRight, step = 0, nums[0], 0
        while i  < len(nums):
            step += 1
            if maxRight >= len(nums)-1:
                return step
            nextMaxRight = maxRight
            for j in range(i+1, maxRight+1):
                if nextMaxRight < j + nums[j]:
                    i = j
                    nextMaxRight = j + nums[j]
            maxRight = nextMaxRight

    #pass. 进一步优化。 我们得到的i=j, 是为了得到最优解，下一步应该跳到的地方。所以下一次循环就是从j开始。
    ＃然而，可以继续优化。因为for all i+1<= j <= maxRight, 我们已经检查过了，不会优于j.所以可以改为直接从maxRight开始下一次搜索
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        i, maxRight, step = 0, nums[0], 0
        while i  < len(nums):
            step += 1
            if maxRight >= len(nums)-1:
                return step
            nextMaxRight = maxRight
            for j in range(i+1, maxRight+1):
                nextMaxRight = max(nextMaxRight, j + nums[j])
            i = maxRight
            maxRight = nextMaxRight

