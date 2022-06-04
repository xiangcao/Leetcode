class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 0 
        right = num/2
        while left < right:
            mid = left + (right-left)/2
            product = mid * mid
            print("product: %s, left: %s, right:%s, mid: %s" %(product, left, right, mid))
            if product == num:
                return True
            elif product > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

m = Solution()
m.isPerfectSquare(4)
