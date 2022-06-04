class Logger:
    # Two Map Solution
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapNew={}
        self.mapOld={}
        self.newStart = float("-inf")

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp - self.newStart >= 20:
            self.mapNew.clear()
            self.mapOld.clear()
            self.newStart = timestamp
        elif timestamp - self.newStart >= 10:
            self.mapOld.clear()
            self.mapOld = self.mapNew
            self.mapNew= {}
            self.newStart = timestamp

        if message in self.mapNew:
            return False
        if message in self.mapOld and timestamp - self.mapOld[message]  < 10:
            return False

        self.mapNew[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

    # Circular Buffer solution
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucketToTime=[0] * 10
        self.bucketToMessageSet=[set() for _ in range(10)]

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        idx = timestamp % 10
        if self.bucketToTime[idx] != timestamp:
            self.bucketToTime[idx] = timestamp
            self.bucketToMessageSet[idx].clear()
        for bucket in range(10):
            if message in self.bucketToMessageSet[bucket]:
                if timestamp - self.bucketToTime[bucket] < 10:
                    return False
        self.bucketToMessageSet[idx].add(message)
        return True
            
     # Minor modification. both works
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        idx = timestamp % 10
        for bucket in range(10):
            if timestamp - self.bucketToTime[bucket] >= 10:
                self.bucketToMessageSet[bucket].clear()
            else:
                if message in self.bucketToMessageSet[bucket]:
                    return False
        self.bucketToTime[idx] = timestamp
        self.bucketToMessageSet[idx].add(message)
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
