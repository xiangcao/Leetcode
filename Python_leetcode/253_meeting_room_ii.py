"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2. 

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda k: k.start)
        heap =[]
        for interval in intervals:
            if len(heap) == 0:
                heapq.heappush(heap, interval.end)
            elif heap[0] <= interval.start:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)
            
        return len(heap)
