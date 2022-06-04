"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
"""
Method 1: Stack of Value/Minimum Pairs
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin is None or curMin > x:
            curMin = x
        self.stack.append((x, curMin))
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]

Approach 2: Two stacks
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

Approach 3: Two stacks improved version
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        
        

    def push(self, x: int) -> None:
        
        # We always put the number onto the main stack.
        self.stack.append(x)
        
        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])
            
        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    
    def pop(self) -> None:

        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1
            
        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
            
        # And like before, pop the top of the main stack.
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1][0]   
