"""
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""
"""
The greedy algorithm is that in each step, select the char with highest remaining count if possible (if it is not in the waiting queue). PQ is used to achieve the greedy. A regular queue waitQueue is used to "freeze" previous appeared char in the period of k.

In each iteration, we need to add current char to the waitQueue and also release the char at front of the queue, put back to maxHeap. The "impossible" case happens when the maxHeap is empty but there is still some char in the waitQueue"""

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        frequencies = collections.Counter(s)
        heap = [(-f, c) for c, f in frequencies.items()]
        heapq.heapify(heap)
        waitqueue=collections.deque([])
        result=[]
        while heap:
            neg_f, c = heapq.heappop(heap)
            if neg_f == 0:
                continue
            result.append(c)
            waitqueue.append((neg_f+1, c))
            
            if len(waitqueue) == k:
                heapq.heappush(heap, waitqueue.popleft())
        return "".join(result) if len(result) == len(s) else ""
   #testcase "a", 2
   #testcase "a", 0
        
# round 2; no need to use deque for waitQueue
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        frequencies = collections.Counter(s)
        heap = [(-f, c) for c, f in frequencies.items()]
        heapq.heapify(heap)
        waitqueue=[]
        result=[]
        while heap:
            neg_f, c = heapq.heappop(heap)
            if neg_f == 0:
                continue
            result.append(c)
            waitqueue.append((neg_f+1, c))

            if len(waitqueue) == k:
                for _ in range(k):
                    heapq.heappush(heap, waitqueue.pop())
        return "".join(result) if len(result) == len(s) else ""
