class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second, third = float("inf"), float("inf"), float("inf")
        for n in nums:
            if n <= first:  # Note: should use <=,  not <;  
                first = n 
            elif n <= second:
                second = n
            elif n <= third:
                third = n
                return True
        return False

