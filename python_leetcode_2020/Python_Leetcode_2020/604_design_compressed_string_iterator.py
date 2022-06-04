"""
Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

Implement the StringIterator class:

next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
"""

class StringIterator:

    def __init__(self, compressedString: str):
        self.string = compressedString
        self.idx = 0
        self.char = None
        self.count = 0
        self.total = 0

    def next(self) -> str:
        if not self.hasNext():
            return " "
        if self.count < self.total:
            self.count += 1
            return self.char
        else:
            self.count = 1
            self.char = self.string[self.idx]
            self.idx += 1
            pos = self.idx
            while pos < len(self.string):
                if self.string[pos].isdigit():
                    pos += 1
                else:
                    break
            self.total = int(self.string[self.idx: pos])
            self.idx = pos
            return self.char

    def hasNext(self) -> bool:
        return self.idx < len(self.string) or self.count < self.total


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
