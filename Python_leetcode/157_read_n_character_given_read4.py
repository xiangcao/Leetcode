# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        iteration = n/4
        index = 0 
        for i in range(iteration+1):
            buf4=[""]*4
            cur = read4(buf4)
            if not cur:
                return index
            for i in range(min(n,cur)):
                buf[index] = buf4[i]
                index += 1
                n -= 1
        return index
            
# refer https://leetcode.com/discuss/44743/another-accepted-java-solution
# refer https://leetcode.com/discuss/61942/ap-solution-c-0ms-4lines
# refer https://leetcode.com/discuss/75083/python-solution-with-explainations-and-comments          

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        readByte = 0
        while readByte < n:
            buf4=[""]*4
            curCount = read4(buf4)
            curPointer = 0
            while readByte < n and curPointer < 4:
                buf[readByte] = buf4[curPointer]
                readByte, curPointer = readByte+1, curPointer+1
        return readByte


