"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
"""

class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.unique = collections.OrderedDict()
        self.count = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        return next(iter(self.unique), -1)


    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.count:
            self.unique[value] = True
            self.count.add(value)
        else:
            self.unique.pop(value, None)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
