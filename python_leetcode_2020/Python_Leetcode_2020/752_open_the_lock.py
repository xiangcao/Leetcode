"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""
"""Hints: 
We can think of this problem as a shortest path problem on a graph: there are `10000` nodes (strings `'0000'` to `'9999'`), and there is an edge between two nodes if they differ in one digit, that digit differs by 1 (wrapping around, so `'0'` and `'9'` differ by 1), and if *both* nodes are not in `deadends`.
"""
class Solution:
    # BFS 
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node: str):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        
        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if  node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

# second round
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        queue = collections.deque([(start, 0)])
        deadends = set(deadends)
        visited = {start}
        while queue:
            current, step = queue.popleft()
            if current == target:
                return step
            if current in deadends:
                continue
            for i in range(4):
                for d in (1, -1):
                    newValue = str((int(current[i]) + d ) % 10)
                    nextState = current[:i] + newValue + current[i+1:]
                    if nextState in deadends or nextState in visited:
                        continue
                    visited.add(nextState)
                    queue.append((nextState, step + 1))
