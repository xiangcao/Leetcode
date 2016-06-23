class Solution(object):
    
    #Accepted
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table=set()
        result = []
        for i in nums1:
            table.add(i)
        for i in nums2:
            if i in table:
                result.append(i)
                table.remove(i)
        return result
        
    
    #Accepted  
    def intersection(self, nums1, nums2):
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
                if (i == 0 or nums1[i-1] != nums1[i]):
                    result.append(nums1[i])
                i += 1
                j += 1
        return result
                
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


# refer https://leetcode.com/discuss/103345/three-java-solutions
