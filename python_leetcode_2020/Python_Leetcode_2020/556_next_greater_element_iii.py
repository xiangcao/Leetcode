"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        numbers = list(str(n))
        right = len(numbers)-1
        MAX_INT = 2 << 31 - 1
        while right > 0:
            if numbers[right] > numbers[right-1]:
                break
            right -= 1
        if right > 0:
            larger = right
            while larger < len(numbers) and numbers[larger] > numbers[right-1]:
                larger += 1
            numbers[right-1], numbers[larger-1] = numbers[larger-1], numbers[right-1]
            i = right
            j = len(numbers)-1
            while i < j:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i += 1
                j -= 1
            result = int(''.join(numbers))
            return result if result < MAX_INT else -1
        
        else:
            return -1
        
        
        
