"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

class Solution:
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        
        s_pointer = e_pointer = 0
        room = 0
        while s_pointer < len(intervals):
            if start_times[s_pointer] >= end_times[e_pointer]:
                e_pointer += 1
            else:
                room += 1
            s_pointer += 1
        return room
                
                
#round 2; sort all times; line sweeping
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        self.record = collections.Counter()
        for interval in intervals:
            self.record[interval[0]] += 1
            self.record[interval[1]] -= 1
        rooms = 0
        maxrooms = 0
        for t in sorted(self.record):
            rooms += self.record[t]
            maxrooms = max(maxrooms, rooms)
        return maxrooms
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        self.record = []
        for interval in intervals:
            self.record.append((interval[0],1))
            self.record.append((interval[1], -1))
        rooms = 0
        maxrooms = 0
        for _, increment in sorted(self.record):
            rooms += increment
            maxrooms = max(maxrooms, rooms)
        return maxrooms
