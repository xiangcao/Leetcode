"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 
"""    
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        res = []
        
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1 
                j += 1
                k += 1
                continue
            
            max_ = max(arr1[i], arr2[j], arr3[k])
            
            if arr1[i] < max_:
                i += 1
            
            if arr2[j] < max_:
                j += 1
                
            if arr3[k] < max_:
                k += 1
                
        return res
