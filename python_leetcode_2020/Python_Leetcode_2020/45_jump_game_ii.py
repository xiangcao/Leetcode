class Solution:
    # return minimum jumps need to reach last position
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0 
        
        # max position one could reach starting from index <= i 
        max_pos = nums[0]
        # max positions one could reach inside this jump
        max_steps = nums[0]
        
        jumps = 1
        for i in range(1, n):
            # if to reach this point 
            # one needs one more jump
            if max_pos < i:  # never will happen since there will be end is always reachable. can be removed. 
                return -1
            if max_steps < i:
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i] + i)
                
        return jumps

# great insight: 
This is an implicit bfs solution. i == curEnd means you visited all the items on the current level. Incrementing jumps++ is like incrementing the level you are on. And curEnd = curFarthest is like getting the queue size (level size) for the next level you are traversing.


