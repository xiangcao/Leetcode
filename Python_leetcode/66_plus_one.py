class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #0 + 1
        #9 + 1
        #98 + 8 = 106
        sum = 1 
        i = len(digits) - 1
        while sum and i >=0:
            add = digits[i] +  sum
            digits[i] = add % 10
            sum = add / 10
            i -= 1
        if sum:
            return [sum] + digits
        else:
            return digits
