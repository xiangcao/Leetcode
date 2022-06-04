"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

class Solution:
    # extra array storing counts in two pass
    # 2*N time, N space
    def candy1(self, ratings: List[int]) -> int:    
        size = len(ratings)
        if size <= 1:
                return size

        nums = [1] * size
        for i in range(1, size):
            if(ratings[i]>ratings[i-1]):
                nums[i]=nums[i-1]+1
        for i in range(size-1, 0, -1):
             if(ratings[i-1]>ratings[i]):
                    nums[i-1]=max(nums[i]+1,nums[i-1])

        return sum(nums)

    # constant space; one pass
    # N time, O(1) space
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        prev, total, countDown = 1, 1, 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i-1]:
                if countDown > 0:
                    total += (1+countDown) * countDown // 2
                    if countDown >= prev:
                        total += countDown - prev + 1
                    countDown = 0
                    prev = 1
                prev = 1 if ratings[i] == ratings[i-1] else prev + 1
                total += prev
            else:
                countDown += 1
        if countDown > 0 :
            total += (1+countDown) * countDown // 2
            if countDown >= prev:
                total += countDown - prev + 1
        return total
        
