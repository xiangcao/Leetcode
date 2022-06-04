"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.node = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        k = 1
        cur = self.node
        ans = None
        while cur:
            if random.randrange(count+1) < k:
                ans = cur.val
            cur = cur.next
            count += 1
        return ans
