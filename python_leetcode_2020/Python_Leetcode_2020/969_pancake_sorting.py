"""
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[1...k].
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).
"""
Explanation
Find the index i of the next maximum number x.
Reverse i + 1 numbers, so that the x will be at A[0]
Reverse x numbers, so that x will be at A[x - 1].
Repeat this process N times.

Update:
Actually, I didn't use the condition permutation of [1,2,..., A.length].
I searched in the descending order of A.

Time Complexity:
O(N^2)
"""

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(array, end):
            start = 0
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
        size = len(arr)
        result = []
        for maxValue in range(size, 0, -1):
            for j in range(maxValue):
                if arr[j] == maxValue and j != maxValue-1:
                    reverse(arr, j)
                    reverse(arr, maxValue-1)
                    result.extend([j+1, maxValue])
                    break
        return result
