"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
"""

class Solution:
    # BFS
    def slidingPuzzle(self, board: List[List[int]]) -> int:
       # moves, used, cnt = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}, set(), 0
        moves, used, cnt = {0: [1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4], 4:[1, 3, 5], 5:[2, 4]}, set(), 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]
        while q:
            new = []
            for s, i in q:
                if s == "123450":
                    return cnt
                arr = [c for c in s]
                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        used.add(new_s)
                        new.append((new_s, move))
            cnt += 1
            q = new
        return -1


    # BFS (leetcode solution)
    """
Time Complexity: O(R * C * (R * C)!), where R, C are the number of rows and columns in board. There are O((R * C)!) possible board states.

Space Complexity: O(R * C * (R * C)!).
"""
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        R, C = len(board), len(board[0])
        start = tuple(itertools.chain(*board)) # #(1,2,3,4,5,0)
        queue = collections.deque([(start, start.index(0), 0)])
        seen = {start}

        target = tuple(list(range(1, R*C)) + [0])

        while queue:
            board, posn, depth = queue.popleft()
            if board == target: return depth
            for d in (-1, 1, -C, C):
                nei = posn + d
                if abs(nei//C - posn//C) + abs(nei%C - posn%C) != 1:
                    continue
                if 0 <= nei < R*C:
                    newboard = list(board)
                    newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
                    newt = tuple(newboard)
                    if newt not in seen:
                        seen.add(newt)
                        queue.append((newt, nei, depth+1))

        return -1
