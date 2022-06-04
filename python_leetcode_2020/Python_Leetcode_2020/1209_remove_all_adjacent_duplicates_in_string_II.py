"""
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.
"""


#Approac 5 Two pointers
"""
Here, we copy characters within the same string using the fast and slow pointers. Each time we need to erase k characters, we just move the slow pointer k positions back.
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count=[]
        i = 0
        j = 0
        output = [None] * len(s)
        while i < len(s):
            output[j] = s[i]
            if j != 0 and output[j-1] == output[j]:
                count[-1] += 1
                if count[-1] == k:
                    count.pop()
                    j -= k
            else:
                count.append(1)
            i += 1
            j += 1
        return "".join(output[:j])


# round 2 
    def removeDuplicates(self, s: str, k: int) -> str:
        count=[]
        j = 0
        output = [None] * len(s)
        for i in range(len(s)):
            output[j] = s[i]
            if j != 0 and output[j-1] == output[j]:
                count[-1] += 1
                if count[-1] == k:
                    count.pop()
                    j -= k
            else:
                count.append(1)
            j += 1
        return "".join(output[:j])
