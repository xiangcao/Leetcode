class Solution:
    # use hashmap to record last seen position of each integer
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i, n in enumerate(nums):
            if n in mapping:
                if i - mapping[n] <= k:
                    return True
            mapping[n] = i
        return False

    # use hashset to maintain sliding window of k
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        hashset = set()
        for i, n in enumerate(nums):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            if len(hashset) > k:
                hashset.remove(nums[i-k])
        return False
            
