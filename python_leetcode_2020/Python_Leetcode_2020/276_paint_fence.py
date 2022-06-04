"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
******************************************************************************
If you are painting the ith post, you have two options:

make it different color as i-1th post
make it same color as i-1 th post (if you are allowed!)
simply add these for your answer:
num_ways(i) = num_ways_diff(i) + num_ways_same(i)

Now just think of how to calculate each of those functions.

The first one is easy. If you are painting the ith post, how many ways can you paint it to make it different from the i-1 th post? k-1

num_ways_diff(i) = num_ways(i-1) * (k-1)

The second one is hard, but not so hard when you think about it.

If you are painting the ith post, how many ways can you paint it to make it the same as the i-1th post? At first, we should think the answer is 1 -- it must be whatever color the last one was.

num_ways_same(i) = num_ways(i-1) * 1

But no! This will fail in the cases where painting the last post the same results in three adjacent posts of the same color! We need to consider ONLY the cases where the last two colors were different. But we can do that!

num_ways_diff(i-1) <- all the cases where the i-1th and i-2th are different.

THESE are the cases where can just plop the same color to the end, and no longer worry about causing three in a row to be the same.

num_ways_same(i) = num_ways_diff(i-1) * 1

We sum these for our answer, like I said before:

num_ways(i) = num_ways_diff(i) + num_ways_same(i)
= num_ways(i-1) * (k-1) + num_ways_diff(i-1)

We know how to compute num_ways_diff, so we can substitute:
num_ways(i) = num_ways(i-1) * (k-1) + num_ways(i-2) * (k-1)

We can even simplify a little more:

num_ways(i) = (num_ways(i-1) + num_ways(i-2)) * (k-1)

As a note, trying to intuitively understand that last line is impossible. If you think you understand it intuitively, you are fooling yourself. Only the original equation makes intuitive sense.

Once you have this, the code is trivial (but overall, this problem is not an easy problem, despite the leetcode tag!):
"""
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        dp=[0] * (n+1)
        dp[1] = k
        dp[2] = k * k 
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) * (k - 1)
        return dp[-1]
