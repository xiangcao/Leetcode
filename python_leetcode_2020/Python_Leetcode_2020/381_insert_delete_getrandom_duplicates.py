class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.map = defaultdict(set) # value:idx

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        self.map[val].add(len(self.list)-1)
        return len(self.map[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.map[val]: return False
        idx = self.map[val].pop()
        self.list[idx] = self.list[-1]
        self.map[self.list[idx]].add(idx)
        
        self.map[self.list[idx]].discard(len(self.list)-1)
        self.list.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
