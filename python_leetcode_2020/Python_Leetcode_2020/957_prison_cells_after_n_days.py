"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9

"""
class Solution(object):
    # Brute Force;  Time limit exceeded
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def getNext(cells):
            ret = [0]
            for i in range(1, len(cells)-1):
                ret.append(int(cells[i-1] == cells[i+1]))
            ret.append(0)
            return ret
        
        while N > 0:
            N-=1
            cells = getNext(cells)
        return cells
      
    # when N is much larger than len(cells), the states must repeat
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def getNext(cells):
            ret = [0]
            for i in range(1, len(cells)-1):
                ret.append(int(cells[i-1] == cells[i+1]))
            ret.append(0)
            return ret
        seen = {}
        is_fast_forwarded = False
        while N > 0:
            if not is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    N %= seen[state_key] - N
                    is_fast_forward = True
                else:
                    seen[state_key] = N
            if N > 0:
                N-=1
                cells = getNext(cells)
        return cells
