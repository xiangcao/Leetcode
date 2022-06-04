from typing import List
def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // w]
        return False


nums=[2,1]
k = 1
t = 1

def containsNearbyAlmostDuplicate2(nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        window = {}
        b_w = t + 1
        import pdb
        pdb.set_trace()
        for i, v in enumerate(nums):
            bucket = v // b_w
            if bucket in window:
                return True
            if (bucket + 1) in window and abs(v-window[bucket+1]) < b_w:
                return True
            if (bucket - 1) in window and abs(v-window[bucket-1]) < b_w:
                return True
            window[bucket] = v
            if i >= k:  # bug:  i > k  
                window.pop(nums[i-k]//b_w, None)
        return False

nums=[1,5,9,1,5,9]
k = 2
t = 3
containsNearbyAlmostDuplicate2(nums, k, t)
