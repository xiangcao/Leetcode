"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Intuition

If we maintained our events in sorted order, we could check whether an event could be booked in O(\log N)O(logN) time (where NN is the number of events already booked) by binary searching for where the event should be placed. We would also have to insert the event in our sorted structure.

Algorithm

We need a data structure that keeps elements sorted and supports fast insertion. In Java, a TreeMap is the perfect candidate. In Python, we can build our own binary tree structure.

For Java, we will have a TreeMap where the keys are the start of each interval, and the values are the ends of those intervals. When inserting the interval [start, end), we check if there is a conflict on each side with neighboring intervals: we would like calendar.get(prev)) <= start <= end <= next for the booking to be valid (or for prev or next to be null respectively.)

For Python, we will create a binary tree. Each node represents some interval [self.start, self.end) while self.left, self.right represents nodes that are smaller or larger than the current node.

Java code
class MyCalendar {
    
    TreeMap<Integer, Integer> calendar;

    MyCalendar() {
        calendar = new TreeMap();
    }

    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start),
                next = calendar.ceilingKey(start);
        if ((prev == null || calendar.get(prev) <= start) &&
                (next == null || end <= next)) {
            calendar.put(start, end);
            return true;
        }
        return false;
    }
}
"""
# python code
class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
