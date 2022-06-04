"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
 
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        candidates = [size//4, size//2, size * 3 //4]
        # binary search
        def findFirst(target):
            start, end = 0, size
            while start < end:
                mid = start + (end-start) // 2
                if arr[mid] < target:
                    start = mid + 1
                elif arr[mid] > target:
                    end = mid - 1
                else:
                    end = mid
            return end
                    
        for candidate in candidates:
            first = findFirst(arr[candidate])
            if arr[first + size//4 ] == arr[candidate]:
                return arr[candidate]
            
# optimization
# only need to search between [i-n/4,i] instead of [0,n) for each of the candidate.
