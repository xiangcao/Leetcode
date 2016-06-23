class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack=[]
        self.data_stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data_stack.append(x)
        # notice: <= instead of <. when we add two duplicate smallest number(push 1, push 2, push 1, pop())
        if not self.min_stack or x <= self.min_stack[-1]:  
            self.min_stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.data_stack:
            return 
        i = self.data_stack.pop()
        if i == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data_stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        
