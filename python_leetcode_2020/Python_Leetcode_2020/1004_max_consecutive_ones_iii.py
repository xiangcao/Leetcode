"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?


"""

class Solution(object):
    # Sliding window
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ans = 0
        zero = 0
        l, r = 0, 0
        for r in range(len(A)):
            if (A[r] == 0) :                                         
                zero += 1
            while (zero > K):
                if (A[l] == 0):
                    zero -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans;             

Now let's deal with follow-up, we need to store up to k indexes of zero within the window [l, h] so that we know where to move l next when the window contains more than k zero. If the input stream is infinite, then the output could be extremely large because there could be super long consecutive ones. In that case we can use BigInteger for all indexes. For simplicity, here we will use int
Time: O(n) Space: O(k)

    public int findMaxConsecutiveOnes(int[] nums) {                 
        int max = 0, k = 1; // flip at most k zero
        Queue<Integer> zeroIndex = new LinkedList<>(); 
        for (int l = 0, h = 0; h < nums.length; h++) {
            if (nums[h] == 0)
                zeroIndex.offer(h);
            if (zeroIndex.size() > k)                                   
                l = zeroIndex.poll() + 1;
            max = Math.max(max, h - l + 1);
        }
        return max;                     
    }

python code
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        maxlen = 0
        k = K
        zeroIndex = collections.deque([])
        l, r = 0, 0
        while r < len(A):
            if A[r] == 0:
                zeroIndex.append(r)
            if len(zeroIndex) > k:
                l = zeroIndex.popleft() + 1
            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen
