"""
 The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times. 
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def __init__(self):
        self.buf4counter = 0
        self.buf4pointer = 0
        self.buff4=[""]*4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        readBytes = 0 
        while readBytes < n:
            if self.buf4pointer == 0:
                self.buf4counter = read4(self.buff4)
            if self.buf4counter == 0:
                break
            while readBytes < n and self.buf4pointer < self.buf4counter:
                buf[readBytes] = self.buff4[self.buf4pointer]
                readBytes, self.buf4pointer = readBytes+1, self.buf4pointer+1
            if self.buf4pointer >= self.buf4counter:
                self.buf4pointer = 0
        return readBytes
        
