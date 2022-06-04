class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count >= self.capacity:
            return False
        self.queue[(self.headIndex + self.count) %  self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue[self.headIndex] if self.count > 0 else -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue[(self.headIndex + self.count - 1) % self.capacity] if self.count > 0 else -1 
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity


As a followup question though, an interviewer might ask one to point out a potential defect about the implementation and the solution.

This time, it is not about the space or time complexity, but concurrency. Our circular queue is NOT thread-safe. One could end up with corrupting our data structure in a multi-threaded environment.

For example, here is an execution sequence where we exceed the designed capacity of the queue and overwrite the tail element undesirably.

The above scenario is called race conditions as described in the problem of Print in Order. One can find more concurrency problems to practice on LeetCode.

There are several ways to mitigate the above concurrency problem. Take the function enQueue(int value) as an example, we show how we can make the function thread-safe in the following implementation:

from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        # the additional attribute to protect the access of our queue
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # automatically acquire the lock when entering the block
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
        # automatically release the lock when leaving the block
        return True

# Your MyCircularQueue object will be instantiated and called as such:

# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
