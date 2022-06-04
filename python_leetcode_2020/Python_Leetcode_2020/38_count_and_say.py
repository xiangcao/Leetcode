"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        sequence = ['1']
        for i in range(n-1):
            sequence = self.nextSequence(sequence)
        return ''.join(sequence)

    def nextSequence(self, prevSeq):
        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        for digit in prevSeq[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                # the end of a sub-sequence
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1

        # the end of a sub-sequence
        nextSeq.extend([str(digitCnt), prevDigit])

        return nextSeq

    def countAndSay(self, n: int) -> str:
        def nextSequence(sequence):
            anchor = 0
            result = []
            for read, c in enumerate(sequence):
                if read + 1 == len(sequence) or sequence[read + 1] != c:
                    result.append(str(read - anchor + 1))
                    result.append(sequence[anchor])
                    anchor = read + 1
            return result
        sequence = ['1']
        for i in range(n-1):
            sequence = nextSequence(sequence)
        return "".join(sequence)


# Recursive
class Solution:
    def countAndSay(self, n: int) -> str:
        return ''.join(self.nextSequence(n, ['1']))

    def nextSequence(self, n, prevSeq):
        if n == 1:
            return prevSeq

        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        for digit in prevSeq[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                # the end of a sub-sequence
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1
        
        # the end of a sub-sequence
        nextSeq.extend([str(digitCnt), prevDigit])

        return self.nextSequence(n-1, nextSeq)
