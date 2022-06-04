"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

"""
# this does not work because user could call snap() multiple times without invoking set in between. each snap would return new snap_id which should still be retrievable
class SnapshotArray(object):

    def __init__(self, n):
        self.A = [{} for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index][self.snap_id] =  val

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        if snap_id not in self.A[index]:
            return 0
        return self.A[index][snap_id]

# works
class SnapshotArray(object):
    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
