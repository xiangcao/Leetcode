"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.
"""

from functools import lru_cache

class Solution:
    # The key observation is that we do not need to distinguish x and y, and we don't care whether x and y are positive or negative at all.
    # x+y == 2:  The moment you reach 0,2 or 2,0 or 1,1 (visualize in the real chess board) the knight cannot move further to 0,0 or might go into negative axis, the smartest way is to if you are in (0,2) move the night to (2,1) then from there it could move to (0,0)..this takes 2 move . same applies for (1,1) and (2,0) too..
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None) 
        def DP(x,y):
            if x + y == 0:
                return 0
            elif x + y == 1:
                return 3
            elif x + y == 2:
                return 2
            return min(DP(abs(x-1),abs(y-2)),DP(abs(x-2),abs(y-1)))+1
        return DP(abs(x),abs(y))

# bfs
class Solution {
    private final int[][] DIRECTIONS = new int[][] {{2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};
    
    public int minKnightMoves(int x, int y) {
        x = Math.abs(x);
        y = Math.abs(y);
        
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0});
        
        Set<String> visited = new HashSet<>();
        visited.add("0,0");
        
        int result = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cur = queue.remove();
                int curX = cur[0];
                int curY = cur[1];
                if (curX == x && curY == y) {
                    return result;
                }
                
                for (int[] d : DIRECTIONS) {
                    int newX = curX + d[0];
                    int newY = curY + d[1];
                    if (!visited.contains(newX + "," + newY) && newX >= -1 && newY >= -1) {
                        queue.add(new int[] {newX, newY});
                        visited.add(newX + "," + newY);
                    }
                }
            }
            result++;
        }
        return -1;
    }
}
