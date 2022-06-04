# Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.buf4=['']*4
        self.size4=0
        self.i4 = 0
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        idx = 0
        while idx < n:
            if self.i4 < self.size4:
                buf[idx] = self.buf4[self.i4]
                self.i4 += 1
                idx += 1
            else:
                self.size4 = read4(self.buf4)
                self.i4 = 0
                if self.size4 == 0:
                    break
        return idx 

//Google followup:
Because using inner buffer(buf4) can introduce more memory copy operation, which is very time-consuming.

We need to copy characters from the file directly when there is enough space in the buffer.

When the buffer size is not enough, we first copy the 4B characters to inner buf4. Then we copy from buf4.


//Only available in C
class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    char buf4[4] = {0};
    int  n4 = 0;
    int  i4 = 0;
    
    int read(char *buf, int n) {
        int i = 0;
        while(i < n) {
            // if there are somehing in buf4, read buf4 first
            if(i4 < n4) {
                buf[i++] = buf4[i4++];
            }
            else {
                // if there is enough space in buf
                if(n - i >= 4) {
                    int rlen = read4(buf + i);
                    i += rlen;
                    if(rlen == 0) return i;
                }
                else {
                    n4 = read4(buf4);
                    i4 = 0;
                    if(n4 == 0) return i;
                }
            }
            
        }
        return i;
    }
};


