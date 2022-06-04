"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        counts = [0] * (num+1)
        for i in range(1, num+1):
            counts[i] = counts[i >> 1] + (i & 1)
        return counts

    def countBits2(self, num: int) -> List[int]:
        counts = [0]
        if num > 0:
            while(len(counts) < num+1):
                counts.extend([x+1 for x in counts])
        return counts[:num+1]

