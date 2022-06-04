"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
"""

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    # Time C * LogC, Space: O(N) 
    # N: number of employess; C: number of intervals
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # First Merge Interval
        intervals = [interval for employee in schedule for interval in employee]
        intervals.sort(key = lambda x: x.start)
        
        result = []
        for interval in intervals:
            if not result or result[-1].end < interval.start:
                result.append(interval)
            result[-1].end = max(result[-1].end, interval.end)
        
        # Return the gap between the intervals
        return [Interval(result[i-1].end, result[i].start) for i in range(1, len(result))]
    
    # Priority Queue.
    # Time: O(C Log N)
    # Space O(N)
    # Keep track of the latest time anchor that we don't know of a job overlapping that time.  When we process the earliest occurring job not yet processed, it occurs at time t, by employee e_id, and it was that employee's e_jx'th job. If anchor < t, then there was a free interval Interval(anchor, t).

    def employeeFreeTime(self, avails):
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(avails)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in avails for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, avails[e_id][e_jx].end)
            if e_jx + 1 < len(avails[e_id]):
                heapq.heappush(pq, (avails[e_id][e_jx+1].start, e_id, e_jx+1))

        return ans
    
    # Events (Line Sweep)
    # Time Complexity: O(ClogC)
    # Space O(C)
    def employeeFreeTime(self, avails):
        OPEN, CLOSE = 0, 1

        events = []
        for emp in avails:
            for iv in emp:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))

        events.sort()
        ans = []
        prev = None
        bal = 0
        for t, cmd in events:
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, t))

            bal += 1 if cmd is OPEN else -1
            prev = t

        return ans
