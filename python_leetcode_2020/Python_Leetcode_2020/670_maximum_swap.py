"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Note:
The given number is in the range [0, 108]
"""

class Solution:
    # my solution
    # first iterating backwards to record the index for max number to the right of each index
    #start left, for any index, if there is a bigger number to the right of it, swap current number with that bigger number. 
    def maximumSwap1(self, num: int) -> int:
        num = list(str(num))
        maxindex = -1
        mapping = {}
        for i in reversed(range(len(num))):
            if maxindex == -1 or num[i] > num[maxindex]:
                maxindex = i
            mapping[i] = maxindex
        
        for i in range(len(num)):
            if num[mapping[i]] > num[i]:
                num[mapping[i]], num[i] = num[i], num[mapping[i]]
                break
        return int("".join(num))

    # leetcode solution
    """Intuition

    At each digit of the input number in order, if there is a larger digit that occurs later, we know that the best swap must occur with the digit we are currently considering.
    we will compute last[d] = i; index i is the last occurences of digit d (if it exists)
    Afterwards, when scanning the number from left to right, if there is a larger digit in the future, we will swap it with the largest such digit; if there are multiple such digits, we will swap it with the one that occurs the latest.
   """
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num))) 
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if d in last and last.get(d) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num
            
