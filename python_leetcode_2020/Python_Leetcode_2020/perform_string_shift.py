class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        finalShift = 0
        for item in shift:
            finalShift += item[1] *  (2 *item[0]  - 1)
        finalShift %= len(s)

        while finalShift > 0:
            s = s[-1] + s[:-1]
            finalShift -= 1
        while finalShift < 0:
            s = s[1:] + s[0]
            finalShift += 1
        return s

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for x, y in shift:
            if x == 0:
                move -= y
            else:
                move += y
        move %= len(s)
        return s[-move:] + s[:-move]



"""

31 / 31 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 14 MB
"""


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        string = collections.deque(s)
        finalShift = 0
        for item in shift:
            finalShift += item[1] *  (2 *item[0]  - 1)
        finalShift %= len(s)
        shiftAmount = abs(finalShift)
        for i in range(shiftAmount):
            if finalShift > 0:
                string.appendleft(string.pop())
            if finalShift < 0:
                string.append(string.popleft())
        return "".join(string)

"""
31 / 31 test cases passed.
Status: Accepted
Runtime: 20 ms
Memory Usage: 13.7 MB
"""
