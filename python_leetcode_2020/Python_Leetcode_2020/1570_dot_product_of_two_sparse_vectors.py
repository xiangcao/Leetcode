"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""

class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dict = {i: val for i, val in enumerate(nums) if val != 0 }
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        if len(self.dict) < len(vec.dict):
            A, B = self.dict, vec.dict
        else:
            A, B = vec.dict, self.dict
        
        for i, val in A.items():
            res += val * B.get(i, 0)
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Round 2
class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {index: value for index, value in enumerate(nums) if value}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        if len(self.dict) <= len(vec.dict):
            first, second = self, vec
        else:
            first, second = vec, self
        for index, value in first.dict.items():
            if index in second.dict:
                ans += value * second.dict[index]
        return ans
