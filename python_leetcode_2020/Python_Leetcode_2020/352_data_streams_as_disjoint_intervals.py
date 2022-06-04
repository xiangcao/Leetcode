"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""

class SummaryRanges(object):

    # Runtime: 132 ms, faster than 100.00% of Python online submissions for Data Stream as Disjoint Intervals.
    # Memory Usage: 18.5 M, less than 6.10% of python submissions
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = {}
        self.end = {}
        self.visited = set()
        

    # Time: O(1)
    # Space: O(N), N is the number of unique intervals
    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.visited:
            return
        
        start, end = (val, val)
        if val - 1 in self.end:
            start = self.end[val-1][0]
            self.end.pop(val-1)
        if val + 1 in self.start:
            end = self.start[val+1][1]
            self.start.pop(val+1)
        self.start[start] = (start, end)
        self.end[end] = (start, end)
        self.visited.add(val)
        

    # Time NLogN, N is the number of unique intervals
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return sorted(self.start.values())
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
