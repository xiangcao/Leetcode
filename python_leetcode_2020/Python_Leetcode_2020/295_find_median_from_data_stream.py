""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        # large could have 1 more element than small

    def addNum(self, num: int) -> None:
        if not self.large:
            self.large.append(num)
            return
    
        if num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        elif len(self.small) + 1 < len(self.large):
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def findMedian(self) -> float:
        return self.large[0] if len(self.large) > len(self.small) else (self.large[0] - self.small[0])/ 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""Followup questions comments
Further Thoughts
There are so many ways around this problem, that frankly, it is scary. Here are a few more that I came across:

Buckets! If the numbers in the stream are statistically distributed, then it is easier to keep track of buckets where the median would land, than the entire array. Once you know the correct bucket, simply sort it find the median. If the bucket size is significantly smaller than the size of input processed, this results in huge time saving. @mitbbs8080 has an interesting implementation here: https://leetcode.com/problems/find-median-from-data-stream/discuss/74057/Tired-of-TWO-HEAPSET-solutions-See-this-segment-dividing-solution-(c%2B%2B)

Reservoir Sampling. Following along the lines of using buckets: if the stream is statistically distributed, you can rely on Reservoir Sampling. Basically, if you could maintain just one good bucket (or reservoir) which could hold a representative sample of the entire stream, you could estimate the median of the entire stream from just this one bucket. This means good time and memory performance. Reservoir Sampling lets you do just that. Determining a "good" size for your reservoir? Now, that's a whole other challenge. A good explanation for this can be found in this StackOverflow answer.

Segment Trees are a great data structure if you need to do a lot of insertions or a lot of read queries over a limited range of input values. They allow us to do all such operations fast and in roughly the same amount of time, always. The only problem is that they are far from trivial to implement. Take a look at my introductory article on Segment Trees if you are interested.

Order Statistic Trees are data structures which seem to be tailor-made for this problem. They have all the nice features of a BST, but also let you find the kth order element stored in the tree. They are a pain to implement and no standard interview would require you to code these up. But they are fun to use if they are already implemented in the language of your choice. [5]
"""
