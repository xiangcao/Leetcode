"""Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []
        for c in S:
            if output and output[-1] == c:
                output.pop()
            else:
                output.append(c)
        return "".join(output)
