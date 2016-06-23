class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table = collections.Counter(nums1)
        result=[]
        for i in nums2:
            if i in table and table[i] > 0:
                result.append(i)
                table[i] -= 1
        return result
        
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """        
        nums1.sort()
        nums2.sort()
        i = j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
        return result
