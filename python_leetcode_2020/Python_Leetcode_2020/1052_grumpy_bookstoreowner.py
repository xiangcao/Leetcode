"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""
# sliding window
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        i = win_of_make_satisfied = satisfied = max_make_satisfied = 0
        for c, g in zip(customers, grumpy):
            satisfied += (1 - g) * c
            win_of_make_satisfied += g * c
            if i >= X:
                win_of_make_satisfied -= grumpy[i - X] * customers[i - X]
            max_make_satisfied = max(win_of_make_satisfied, max_make_satisfied)  
            i += 1    
        return satisfied + max_make_satisfied
