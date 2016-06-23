class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        """
if i don't add %26:  
Input: ["az","yx"]
Output: [["az"],["yx"]]
Expected: [["az","yx"]]
Stdout: (0, 25)
(0, -1)

        """
        def mapStr(str):
            result = tuple((ord(l)-ord(str[0]))%26 for l in str)
            return result
        table = collections.defaultdict(list)
        strings.sort()
        for str in strings:
            table[mapStr(str)].append(str)
        return table.values()
            
       #or return map(sorted, table.values()) 

