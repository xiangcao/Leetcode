class Solution(object):
    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        tmp = ['' for i in range(len(s))]
        
        index = -1; step = 1
        for i in range(len(s)):
            index += step
            if index == numRows:
                index -= 2
                step = -1
            elif index == -1:
                index += 2
                step = 1
            tmp[index] += s[i]
        return ''.join(tmp)
    #method 2: http://www.aichengxu.com/view/39454
    def convert(self, s, numRows):
        lists= []
        lens = len(s)
        grp = 2 * numRows - 2 if numRows >=2 else numRows
        
        for iRow in range(numRows):
            sindex = iRow
            while sindex < lens:
                lists.append(s[sindex])
                if iRow > 0 and iRow < (numRows-1):
                    sindex2 = sindex + grp - 2* iRow
                    if sindex2 < lens:
                        lists.append(s[sindex2])
                        
                sindex += grp
                
        return ''.join(lists)
        
