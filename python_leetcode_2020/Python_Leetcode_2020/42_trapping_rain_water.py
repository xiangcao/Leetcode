"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""

class Solution:
    # DP
    """
Approach 2: Dynamic Programming
Intuition

In brute force, we iterate over the left and right parts again and again just to find the highest bar size upto that index. But, this could be stored. Voila, dynamic programming.

Algorithm

Find maximum height of bar from the left end upto an index i in the array \text{left\_max}left_max.
Find maximum height of bar from the right end upto an index i in the array \text{right\_max}right_max.
Iterate over the \text{height}height array and update ans:
Add \min(\text{left\_max}[i],\text{right\_max}[i]) - \text{height}[i]min(left_max[i],right_max[i])−height[i] to \text{ans}ans
"""
int trap(vector<int>& height)
{
    if(height == null)
	return 0;
    int ans = 0;
    int size = height.size();
    vector<int> left_max(size), right_max(size);
    left_max[0] = height[0];
    for (int i = 1; i < size; i++) {
        left_max[i] = max(height[i], left_max[i - 1]);
    }
    right_max[size - 1] = height[size - 1];
    for (int i = size - 2; i >= 0; i--) {
        right_max[i] = max(height[i], right_max[i + 1]);
    }
    for (int i = 1; i < size - 1; i++) {
        ans += min(left_max[i], right_max[i]) - height[i];
    }
    return ans;
}
    # two pointer solution on leetcode
    # if there is a larger bar on right end, we are assured the water trapped on current bar is decided by the left higest bar;
    # if there is a larger bar on left end, the water trapped on current bar is decided by the right highest bar
    def trap(self, height: List[int]) -> int:
        left, right=0, len(height)-1;
        res=0;
        maxleft = maxright = 0
        while left <= right:
            if height[left] <= height[right]:
                if(height[left]>=maxleft):
                    maxleft = height[left]
                else:
                    res+=maxleft-height[left]
                left += 1
            else:
                if(height[right]>=maxright):
                    maxright= height[right]
                else:
                    res+=maxright-height[right]
                right -= 1
        return res

    # two pointer solution inspired by the priority queue solution in 407 trapping rain water II
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                ans += max(0, height[left] - height[left+1])
                height[left+1] = max(height[left+1], height[left])
                left += 1
            else:
                ans += max(0, height[right] - height[right-1])
                height[right-1] = max(height[right-1], height[right])
                right -= 1
        return ans
    
    
        
