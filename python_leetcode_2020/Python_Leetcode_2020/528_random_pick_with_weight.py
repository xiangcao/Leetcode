"You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).
"""
class Solution:

    def __init__(self, w: List[int]):
        self.runningSum = []
        for i, weight in enumerate(w):
            if not self.runningSum:
                self.runningSum.append(weight)
            else:
                self.runningSum.append(weight + self.runningSum[-1])

    # linear search: 5844ms
    # binary search: 232 ms
    def pickIndex(self) -> int:
        # start range from 1; in this case, we need to find the first prefix sum that is larger than or equal to the generated number
        number = random.randint(1, self.runningSum[-1]) # This is tricky;  the range must start from 1;  if you do random.randint(0, self.runningSum[-1]), it is wrong. ;  see solution 3 where the range is changed to start from 0
        left, right = 0, len(self.runningSum)
        while left < right:
            mid = left + (right-left)//2
            if self.runningSum[mid] == number:
                return mid
            elif self.runningSum[mid] < number:
                left = mid + 1
            else:
                right = mid
        return left
        #return bisect.bisect_left(self.runningSum, number)  #pass
        #for i, val in enumerate(self.runningSum):   # pass
        #    if number <= val:
        #        return i

    # 300 ms
    def pickIndex(self) -> int:
        number = random.randint(0, self.runningSum[-1]-1)
        left, right = 0, len(self.runningSum)
        while left < right:
            mid = left + (right-left)//2
            if self.runningSum[mid] <= number:
                left = mid + 1
            else:
                right = mid
        return left
    
class Solution:
    # 240 ms
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
