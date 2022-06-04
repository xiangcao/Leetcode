"""
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
"""
class Solution:
    # O(logn + k)
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-1
        if x > arr[right]:
            return arr[right+1-k:right+1]
        if x < arr[left]:
            return arr[:k]
        # next three lines are optimization; still correct without them
        i = bisect.bisect_left(arr, x)
        left = max(0, i - k)
        right = min(len(arr)-1, i + k -1 )
        
        while right - left + 1 > k:
            if x - arr[left] > arr[right] - x:
                left += 1
            else:  # when equal, prefer smaller element
                right -= 1
        return arr[left:right+1]
    
    # O(Log(N-k) + k)
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else: 
                right = mid
        return A[left:left + k]        

#explanation for the 2nd approach
ntuition
The array is sorted.
If we want find the one number closest to x,
we don't have to check one by one.
it's straightforward to use binary research.

Now we want the k closest,
the logic should be similar.


Explanation
Assume we are taking A[i] ~ A[i + k -1].
We can binary research i
We compare the distance between x - A[mid] and A[mid + k] - x

@vincent_gui listed the following cases:
Assume A[mid] ~ A[mid + k] is sliding window

case 1: x - A[mid] < A[mid + k] - x, need to move window go left
-------x----A[mid]-----------------A[mid + k]----------

case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
-------A[mid]----x-----------------A[mid + k]----------

case 3: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]------------------x---A[mid + k]----------

case 4: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]---------------------A[mid + k]----x------

If x - A[mid] > A[mid + k] - x,
it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
and we have mid smaller than the right i.
So assign left = mid + 1.

Important
Note that, you SHOULD NOT compare the absolute value of abs(x - A[mid]) and abs(A[mid + k] - x).
It fails at cases like A = [1,1,2,2,2,2,2,3,3], x = 3, k = 3

The problem is interesting and good.
Unfortunately the test cases is terrible.
The worst part of Leetcode test cases is that,
you submit a wrong solution but get accepted.

You didn't read my post and up-vote carefully,
then you miss this key point.


Complexity
Time O(log(N - K)) to binary research and find result
Space O(K) to create the returned list.


