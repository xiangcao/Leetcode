class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        A = self.M[key]
        if not A:
            return ""
        i = bisect.bisect(A, (timestamp, chr(255)))
        if i == 0:
            return ""
        else:
            return A[i-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
