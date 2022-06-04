"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?

"""
def threeSumSmaller(self, nums, target):
    count = 0
    nums.sort()
    for i in xrange(len(nums)):
        j, k = i+1, len(nums)-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                # (i,j,j+1) all work, totally (k-j) triplets
                count += k-j
                j += 1
            else:
                k -= 1
    return count
