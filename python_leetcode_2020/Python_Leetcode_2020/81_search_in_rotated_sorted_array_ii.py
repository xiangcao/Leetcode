# allow duplicates
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            # the only difference from the first one, trickly case, just updat left and right
            if( (nums[start] == nums[mid]) and (nums[end] == nums[mid])):
                start += 1
                end -= 1
            elif nums[mid] < nums[start]:
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return False
