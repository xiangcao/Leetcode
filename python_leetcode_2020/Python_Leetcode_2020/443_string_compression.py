"""Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        while j < len(chars):
            count = 0
            curChar = chars[j]
            while j < len(chars) and chars[j] == curChar:
                j += 1
                count += 1
            chars[i] = curChar
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
        return i

# 2nd round
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        length = 1
        while read < len(chars):
            if read == len(chars)-1 or chars[read] != chars[read+1]:
                if length == 1:
                    chars[write] = chars[read]
                    write += 1
                    read += 1
                else:
                    output = chars[read] + str(length)
                    for i in range(len(output)):
                        chars[write] = output[i]
                        write += 1
                    read += 1
                    length = 1
            else:
                read += 1
                length += 1
        return write
                    
                
