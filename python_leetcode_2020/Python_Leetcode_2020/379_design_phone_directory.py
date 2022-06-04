"""
Design a Phone Directory which supports the following operations:
 
get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.

Example:
// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// Assume it returns 0
directory.get();

// The number 0 is no longer available, so return false.
directory.check(0);

// Release number 0 back to the pool.
directory.release(0);

// Number 0 is available again, return true.
directory.check(0);

Constraints:

1 <= maxNumbers <= 10^4
0 <= number < maxNumbers
The total number of call of the methods is between [0 - 20000]
"""
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.next = [(i+1) % maxNumbers for i in range(maxNumbers)]
        self.pos = 0

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.next[self.pos] == -1:
            return -1
        result = self.pos
        self.pos = self.next[self.pos]
        self.next[result] = -1
        return result

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return self.next[number] != -1

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if self.next[number] != -1:
            return
        self.next[number] = self.pos
        self.pos = number
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
