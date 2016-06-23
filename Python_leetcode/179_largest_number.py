class Solution:
    # @param {integer[]} nums
    # @return {string}
    """ 
    Input: [121,12]
    Output: "12112"
    Expected: "12121" 
    
    """
    def largestNumber(self, nums):
        nums = map(str, nums)
        nums.sort(cmp=lambda x,y: cmp(x+y, y+x), reverse=True)
        return ''.join(nums).lstrip('0') or '0'
    
