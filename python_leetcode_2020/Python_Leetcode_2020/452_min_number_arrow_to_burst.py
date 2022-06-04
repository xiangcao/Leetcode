"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.
"""

# Greedy

class Solution:
    #sort by end position
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrow = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            if x_start > first_end:
                arrow += 1
                first_end = x_end
        return arrow
    
    #We can sort it from start position as well:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])

        ans = 1
        end = points[0][1]
        for point in points:
            if(point[0] <= end):
                end = min(end, point[1])
            else:
                end = point[1]
                ans += 1
        return ans

Here I provide a concise template that I summarize for the so-called "Overlapping Interval Problem", e.g. Minimum Number of Arrows to Burst Balloons, and Non-overlapping Intervals etc. I found these problems share some similarities on their solutions.

Sort intervals/pairs in increasing order of the start position.
Scan the sorted intervals, and maintain an "active set" for overlapping intervals. At most times, we do not need to use an explicit set to store them. Instead, we just need to maintain several key parameters, e.g. the number of overlapping intervals (count), the minimum ending point among all overlapping intervals (minEnd).
If the interval that we are currently checking overlaps with the active set, which can be characterized by cur.start > minEnd, we need to renew those key parameters or change some states.
If the current interval does not overlap with the active set, we just drop current active set, record some parameters, and create a new active set that contains the current interval.
int count = 0; // Global parameters that are useful for results.
int minEnd = INT_MAX; // Key parameters characterizing the "active set" for overlapping intervals, e.g. the minimum ending point among all overlapping intervals.
sort(points.begin(), points.end()); // Sorting the intervals/pairs in ascending order of its starting point
for each interval {
      if(interval.start > minEnd) { // If the 
	 // changing some states, record some information, and start a new active set. 
	count++;
	minEnd = p.second;
      }
     else {
	// renew key parameters of the active set
	minEnd = min(minEnd, p.second);
      } 
 }
return the result recorded in or calculated from the global information;
For example, for the problem Minimum "Number of Arrows to Burst Balloons", we have

Sort balloons in increasing order of the start position.
Scan the sorted pairs, and maintain a pointer for the minimum end position for current "active balloons", whose diameters are overlapping.
When the next balloon starts after all active balloons, shoot an arrow to burst all active balloons, and start to record next active balloons.
int findMinArrowShots(vector<pair<int, int>>& points) {
        int count = 0, minEnd = INT_MAX;
        sort(points.begin(), points.end());
        for(auto& p: points) {
            if(p.first > minEnd) {count++; minEnd = p.second;}
            else minEnd = min(minEnd, p.second);
        }
        return count + !points.empty();
    }
For the problem "Non-overlapping Intervals", we have

int eraseOverlapIntervals(vector<Interval>& intervals) {
        int total = 0, minEnd = INT_MIN, overNb = 1;
        sort(intervals.begin(), intervals.end(), [&](Interval& inter1, Interval& inter2) {return inter1.start < inter2.start;});
        for(auto& p: intervals) {
            if(p.start >= minEnd) {
                total += overNb-1;
                overNb = 1;
                minEnd = p.end;
            }
            else {
                overNb++;
                minEnd = min(minEnd, p.end);
            }
        }
        return total + overNb-1;
    }

python:
    #[[1,2]],  output: 0
    #[[1,2],[2,3]], output: 0
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        minEnd = float("-inf")
        result = 0
        overlapping = 1
        for interval in intervals:
            if interval[0] >= minEnd:
                minEnd = interval[1]
                result += overlapping-1
                overlapping = 1
            else:
                overlapping += 1
                minEnd = min(minEnd, interval[1])
        return result + overlapping - 1
