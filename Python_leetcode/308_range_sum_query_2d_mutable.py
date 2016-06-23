"""
https://leetcode.com/discuss/71025/c-quad-tree-736ms-and-indexed-tree-492ms-based-solutions


Your "segment tree" implementation is Quad-Tree. Quad-Tree != 2D segment tree. http://codeforces.com/blog/entry/16363

For Quad-Tree, the worst case time complexity is O(max(n, m)), not O(log(mn)). http://apps.topcoder.com/forums/?module=Thread&threadID=633075

A real 2D segment tree implementation will have time complexity O(logm * logn), which is the same as 2D binary indexed tree. http://e-maxx.ru/algo/segment_tree

############
#https://leetcode.com/discuss/79315/bit-python-clean-code
#don't use update when constructing BIT
# https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/#2d 

Basic idea
Each integer can be represented as sum of powers of two. In the same way, cumulative frequency can be represented as sum of sets of subfrequencies. In our case, each set contains some successive number of non-overlapping frequencies.

idx is some index of BIT. r is a position in idx of the last digit 1 (from left to right) in binary notation. tree[idx] is sum of frequencies from index (idx – 2^r + 1) to index idx (look at the Table 1.1 for clarification). We also write that idx is responsible for indexes from (idx - 2^r + 1) to idx (note that responsibility is the key in our algorithm and is the way of manipulating the tree).

class BIT(object):
    def __init__(self, matrix):
        m = len(matrix)
        if m == 0: n = 0
        else:
            n = len(matrix[0])
        self.matrix = matrix
        self.sums = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for row in range(1, m+1):
            for col in range(1, n+1):
                for i in range(row+1-(row&-row), row+1):
                    for j in range(col+1-(col & -col), col+1):
                        self.sums[row][col] += matrix[i-1][j-1]
                        
    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        i = row+1
        while i < len(self.sums):
            j = col + 1
            while j < len(self.sums[0]):
                self.sums[i][j] += delta
                j += j & (-j)
            i += i & (-i)
        self.matrix[row][col] = val
        
    def sum(self, row, col):
        sum = 0 
        i = row
        while i > 0:
            j = col
            while j > 0:
                sum  += self.sums[i][j]
                j -= j & (-j)
            i -= i & (-i)
        
        return sum
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.tree = BIT(matrix)
        
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.tree.update(row, col, val)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.tree.sum(row2+1, col2+1) - self.tree.sum(row1, col2+1) - self.tree.sum(row2+1, col1) + self.tree.sum(row1, col1)
        
############################################################
#https://leetcode.com/discuss/71169/java-2d-binary-indexed-tree-solution-clean-and-short-17ms
#reuse update() to construct bit

public class NumMatrix {

    int[][] tree;
    int[][] nums;
    int m;
    int n;

    public NumMatrix(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;
        m = matrix.length;
        n = matrix[0].length;
        tree = new int[m+1][n+1];
        nums = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                update(i, j, matrix[i][j]);
            }
        }
    }

    public void update(int row, int col, int val) {
        if (m == 0 || n == 0) return;
        int delta = val - nums[row][col];
        nums[row][col] = val;
        for (int i = row + 1; i <= m; i += i & (-i)) {
            for (int j = col + 1; j <= n; j += j & (-j)) {
                tree[i][j] += delta;
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        if (m == 0 || n == 0) return 0;
        return sum(row2+1, col2+1) + sum(row1, col1) - sum(row1, col2+1) - sum(row2+1, col1);
    }

    public int sum(int row, int col) {
        int sum = 0;
        for (int i = row; i > 0; i -= i & (-i)) {
            for (int j = col; j > 0; j -= j & (-j)) {
                sum += tree[i][j];
            }
        }
        return sum;
    }
}
// time should be O(log(m) * log(n))
############################################################
https://leetcode.com/discuss/97251/python-simple-sum-array-one-dimension-for-both-update-and-sum

the matrix is m-by-n, the time complexity of insert is O(n), and the time complexity for sum is O(m)

"""


#tutorial https://www.hackerearth.com/notes/binary-indexed-tree-or-fenwick-tree/
# https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/ 
