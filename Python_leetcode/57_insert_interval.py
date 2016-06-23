# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        #sortedIntervals = sorted(intervals, key=labmda x: x.start)
        if len(intervals) == 0:
            return [newInterval]
        left, right = 0, len(intervals)-1
        #find the last element with smaller or equal start time 
        while left < right:
            mid = left + (right-left+1)/2
            if intervals[mid].start <= newInterval.start:
                left = mid
            else:
                right = mid - 1
        if intervals[left].start > newInterval.start:
            intervals[left], newInterval = newInterval, intervals[left] 
        print "left is ", left
        if newInterval.start > intervals[left].end:
            intervals.insert(left+1, newInterval)
            left = left+1
            unmergedEnd = newInterval.end
        else:
            unmergedEnd = max(newInterval.end, intervals[left].end)
        #find the first disjoint after insert position
        i = left + 1
        while i <  len(intervals):
            if intervals[i].start <= unmergedEnd: # = is necesssary. see testcase 5 below
                unmergedEnd = max(unmergedEnd, intervals[i].end)
            else:
                break
            i += 1
        intervals[left].end = unmergedEnd
        return intervals[:left+1] + intervals[i:]
        
        #testcase [[1,5]], [2, 7]
        #testcase [[1,5]] [0,3]
        #testcase [[2,5]] [0,1]
        #testcase [], [1,2]
        #testcase [[1,5],[6,8]], [5,6]  
