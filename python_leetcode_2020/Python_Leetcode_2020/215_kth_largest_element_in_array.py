#https://leetcode.com/problems/kth-largest-element-in-an-array/solution/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot):
            nums[right], nums[pivot] = nums[pivot], nums[right]
            store_index = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[store_index], nums[right] = nums[right], nums[store_index]      
            return store_index
        def select(left, right, k):
            if left == right:
                return nums[left]
            # pivot = left
            pivot = random.randint(left, right) 
            partition_index = partition(left, right, pivot)
            if partition_index == k-1:
                return nums[k-1]
            elif partition_index > k - 1:
                return select(left, partition_index-1, k)
            else:
                return select(partition_index+1, right, k)
        return select(0, len(nums)-1, len(nums)-k+1)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
