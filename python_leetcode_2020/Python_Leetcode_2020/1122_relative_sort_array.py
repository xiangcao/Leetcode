class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, cnt = [], collections.Counter(arr1)         # Count each number in arr1
        for i in arr2:
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the common numbers in both arrays by the order of arr2. 
        for i in range(1001):               
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the numbers only in arr1.
        return ans
