class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucketToTime = [-1] * 300
        self.bucketToCount = [0] * 300
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % 300
        if self.bucketToTime[idx] != timestamp:
            self.bucketToTime[idx] = timestamp
            self.bucketToCount[idx] = 1
        else:
            self.bucketToCount[idx] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        result = 0
        for i in range(300):
            if timestamp - self.bucketToTime[i] < 300:
                result += self.bucketToCount[i]
        return result


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
