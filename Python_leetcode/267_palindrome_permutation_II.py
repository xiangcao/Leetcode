class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        exist=set()
        sequence=[]
        for i in s:
            if i in exist:
                exist.remove(i)
                sequence.append(i)
            else:
                exist.add(i)
        if len(exist) > 1: return []
            
        sequence.sort()
       
        #permutaiotn II  
        def permutation(sequence):
            '''
            :rtype List[List[str]]
            '''
            if len(sequence) < 2:
                return [sequence]
            firsthalfpermutations = []
            for i in range(len(sequence)):
                if i > 0 and sequence[i] == sequence[i-1]: continue
                for perm in permutation(sequence[:i]+sequence[i+1:]):
                    firsthalfpermutations.append(perm + [sequence[i]])
            return firsthalfpermutations
                
        firsthalfpermutations = permutation(sequence)
        finalresult=[]
        for firsthalf in firsthalfpermutations:
            if len(exist) == 1: 
                finalresult += [firsthalf + [max(exist)] + firsthalf[::-1]]
            else:
                finalresult += [firsthalf + firsthalf[::-1]]
        
        return [''.join(res) for res in finalresult]
 
