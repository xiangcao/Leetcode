/*
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
*/

class Solution {
  class myComparator implements Comparator<int[]> {
    public int compare(int[] a, int[] b) {
      return a[1] - b[1];
    }
  }

  public int eraseOverlapIntervals(int[][] intervals) {
    if (intervals.length == 0) {
      return 0;
    }
    Arrays.sort(intervals, new myComparator());
    int end = intervals[0][1], prev = 0, count = 0;
    for (int i = 1; i < intervals.length; i++) {
      if (intervals[prev][1] > intervals[i][0]) {
        if (intervals[prev][1] > intervals[i][1]) {
          prev = i;
        }
        count++;
      } else {
        prev = i;
      }
    }
    return count;
  }
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
