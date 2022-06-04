"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""

"""Main idea is to maintain a list of Bucket's, each Bucket contains all keys with the same count.

head and tail can ensure both getMaxKey() and getMaxKey() be done in O(1).
keyCountMap maintains the count of keys, countBucketMap provides O(1) access to a specific Bucket with given count. Deleting and adding a Bucket in the Bucket list cost O(1), so both inc() and dec() take strict O(1) time.
"""
# each Bucket contains all the keys with the same count
class Bucket:
    def __init__(self, cnt):
        self.count = cnt
        self.keySet = set()
        self.next = self.pre = None

class AllOne:  
    def __init__(self):
        self.head = Bucket(float("-inf"))
        self.tail = Bucket(float("inf"))
        self.head.next = self.tail
        self.tail.pre = self.head
        self.countBucketMap = {}
        self.keyCountMap = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key in self.keyCountMap:
            self._updateCount(key, 1)
        else:
            self.keyCountMap[key] = 1
            if self.head.next.count != 1:
                self._addBucketAfter(Bucket(1), self.head)
            self.head.next.keySet.add(key)
            self.countBucketMap[1] = self.head.next

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.keyCountMap:
            return
        self._updateCount(key, -1)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail.pre == self.head:
            return "" 
        else:
            key = self.tail.pre.keySet.pop()
            self.tail.pre.keySet.add(key)
            return key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next == self.tail:
            return "" 
        else:
            key = self.head.next.keySet.pop()
            self.head.next.keySet.add(key)
            return key

    def _addBucketAfter(self, nodeA, preBucket):
        preBucket.next.pre = nodeA
        nodeA.next = preBucket.next
        nodeA.pre = preBucket
        preBucket.next = nodeA

    def _removeKeyFromBucket(self, bucket, key):
        bucket.keySet.remove(key)
        if len(bucket.keySet) == 0:
            self._removeBucketFromList(bucket)
            self.countBucketMap.pop(bucket.count)
    
    def _removeBucketFromList(self, bucket):
        bucket.pre.next = bucket.next
        bucket.next.pre = bucket.pre
        bucket.next = None
        bucket.pre = None
            
    def _updateCount(self, key, countChange):
        cur_count = self.keyCountMap[key]
        new_count = cur_count + countChange
        cur_bucket = self.countBucketMap[cur_count]
        if new_count == 0:
            self.keyCountMap.pop(key)

            self._removeKeyFromBucket(cur_bucket, key)
        elif new_count in self.countBucketMap:
            self.keyCountMap[key] = new_count

            self.countBucketMap[new_count].keySet.add(key)
            self._removeKeyFromBucket(cur_bucket, key)
        else:
            self.keyCountMap[key] = new_count
            new_bucket = Bucket(new_count)
            self.countBucketMap[new_count] = new_bucket
            self._addBucketAfter(new_bucket, cur_bucket if countChange > 0 else cur_bucket.pre)
 
            self.countBucketMap[new_count].keySet.add(key)
            self._removeKeyFromBucket(cur_bucket, key)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
