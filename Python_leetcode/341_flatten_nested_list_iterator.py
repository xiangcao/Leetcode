# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#Refer StefanPochmann's solution:  https://leetcode.com/discuss/95934/real-iterator-in-python-java-c

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]  #[curlist, curlistinternalindex]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        curlist, curlistpos = self.stack[-1]
        self.stack[-1][1] += 1
        return curlist[curlistpos].getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            curlist, curlistpos = self.stack[-1]
            if curlistpos < len(curlist):
                if curlist[curlistpos].isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([curlist[curlistpos].getList(), 0])
            else:
                self.stack.pop()
        return False
                
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
