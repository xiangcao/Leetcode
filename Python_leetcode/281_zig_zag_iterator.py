class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.turn = 0
        self.data = [v1,v2]
        self.index = [0,0]

    def next(self):
        """
        :rtype: int
        """
        result = self.data[self.turn][self.index[self.turn]]
        self.index[self.turn] += 1
        self.turn = 1- self.turn
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        for i in range(len(self.data)):
            curindex = self.index[self.turn]
            curvec = self.data[self.turn]
            if curindex >= len(curvec):
                self.turn = 1- self.turn
                continue
            else:
                return True
        return False
            

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
