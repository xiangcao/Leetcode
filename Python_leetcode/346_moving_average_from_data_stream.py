class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.maxsize = size
        self.sum = 0
        self.window = collections.deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.append(val)
        if len(self.window) < self.maxsize:
            self.sum += val
        else:
            self.sum += val - self.window.popleft()
            
        return self.sum/self.maxsize
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
