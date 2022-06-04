"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class Solution(object):
    # Wrong
    def backspaceCompareBuggy(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = 0 
        while i < len(S) and i < len(T):
            if S[-1-i] != T[-1-i]:
                return False
            if S[-1-i] == '#':
                i += 1
            i += 1
        
        if i < len(S):
            return S[-1-i] == '#'
        if i < len(T):
            return T[-1-i] == '#'
        return True

s = Solution()
print(s.backspaceCompareBuggy("ab#c", "ad#c"))
print(s.backspaceCompareBuggy("ab##","c#d#"))

    # correct 1
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S)-1, len(T) - 1
        backS = backT = 0
        while True:
            while (i >= 0 and (S[i] == '#' or backS > 0)):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while (j >= 0 and (T[j] == '#' or backT > 0)):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if (i >= 0  and j >= 0 and S[i] == T[j]):
                i -= 1
                j -= 1
                continue
            else:
                return i == -1 and j == -1

    #correct 2 use generator
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(s):
            skip = 0
            for x in reversed(s):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
                    
        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
""" python doc 
itertools.zip_longest(*iterables, fillvalue=None)
Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted. Roughly equivalent to:

def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)
If one of the iterables is potentially infinite, then the zip_longest() function should be wrapped with something that limits the number of calls (for example islice() or takewhile()). If not specified, fillvalue defaults to None.
"""
