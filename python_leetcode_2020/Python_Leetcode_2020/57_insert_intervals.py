class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] < newInterval[0]:
                result.append(intervals[i])
                i += 1
            else:
                break
        if not result or result[-1][1] < newInterval[0]:
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], newInterval[1])
        
        while i < len(intervals):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            i+=1
        return result
