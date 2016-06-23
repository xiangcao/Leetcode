class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        #[1,3,3] -> [1,3,3], [3,1,3], [3,3,1]
        result=[]
        def _permute(index):
            if index == len(nums):
                result.append(copy.deepcopy(nums))
            for i in range(index, len(nums)):
                # if anything from nums[index] to nums[i-1] is equal to nums[i], don't swap nums[indx] with nums[i]
                duplic = [ j for j in range(index, i) if nums[j] == nums[i]]
                if duplic == []:
                    #we should swap nums[i] and nums[index]
                    nums[i], nums[index] = nums[index], nums[i]
                    _permute(index+1)
                    nums[i], nums[index] = nums[index], nums[i]
        _permute(0)
        return result

    #very similar to the approach used for subset II     
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])
        if nums is None:
            return []
        result = []
        _permute(result, [], sorted(nums))
        return result


    def permuteUnique(self, sequence):
        '''
        :rtype List[List[int]]
        '''
        if len(sequence) < 2:
            return [sequence]
        firsthalfpermutations = []
        sequence.sort()
        for i in range(len(sequence)):
            if i > 0 and sequence[i] == sequence[i-1]: continue
            for perm in self.permuteUnique(sequence[:i]+sequence[i+1:]):
                firsthalfpermutations.append(perm + [sequence[i]])
        return firsthalfpermutations
