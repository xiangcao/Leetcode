"""
Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
"""

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        answer = []
        m = collections.defaultdict(list)
        maxKey = 0 # maximum key inserted into the map i.e. max value of i+j indices.
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                m[i+j].append(nums[i][j]) # insert nums[i][j] in bucket (i+j).
                maxKey = max(maxKey, i+j)
        for i in range(maxKey+1): # Each diagonal starting with sum 0 to sum maxKey.
            answer.extend(m[i][::-1])

        return answer
