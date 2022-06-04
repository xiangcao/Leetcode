class Solution(object):
    #Time complexity : O(n^2); Two nested loops are there.
    #Space complexity : O(n^2); hashmap size can grow upto n^2n 
2
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        mapping = {}
        for s in stones:
            mapping[s] = set()
    
        mapping[0].add(0)
        for s in stones:
            for pre_jump in mapping[s]:
                for new_jump in (pre_jump-1, pre_jump+1, pre_jump):
                    if new_jump and s + new_jump in mapping:
                        mapping[s+new_jump].add(new_jump)
        return len(mapping[stones[-1]]) > 0
                    
