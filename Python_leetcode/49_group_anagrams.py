class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table={}
        strs.sort()
        for str in strs:
            key = ''.join(sorted(str))
            if table.get(key):
               table[key].append(str)
            else:
                table[key] = [str]
        
        return table.values()
