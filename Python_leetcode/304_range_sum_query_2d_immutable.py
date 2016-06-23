class NumMatrix(object):

    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    matrix[i][j] = matrix[i][j-1] + matrix[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j]
                else:
                    matrix[i][j] = matrix[i-1][j] + (matrix[i][j-1]-matrix[i-1][j-1]) + matrix[i][j]
        self.matrix = matrix
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        if row1 == 0:
            topExtra = 0
        else:
            topExtra = self.matrix[row1-1][col2]
        if col1 == 0:
            leftExtra = 0 
        else:
            leftExtra = self.matrix[row2][col1-1]
            
        if row1 == 0 or col1 == 0:
            leftTop = 0
        else:
            leftTop = self.matrix[row1-1][col1-1]
        return self.matrix[row2][col2] -  leftExtra - topExtra + leftTop
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)


"""
refer this solution which avoids edge case checking:

https://leetcode.com/discuss/69424/clean-c-solution-and-explaination-o-mn-space-with-o-1-time
https://leetcode.com/discuss/69045/sharing-my-python-solution

(notice: we add additional blank row sums[0][col+1]={0} and blank column sums[row+1][0]={0} to remove the edge case checking), so, we can have the following definition

sums[i+1][j+1] represents the sum of area from matrix[0][0] to matrix[i][j]

class NumMatrix {
private:
    int row, col;
    vector<vector<int>> sums;
public:
    NumMatrix(vector<vector<int>> &matrix) {
        row = matrix.size();
        col = row>0 ? matrix[0].size() : 0;
        sums = vector<vector<int>>(row+1, vector<int>(col+1, 0));
        for(int i=1; i<=row; i++) {
            for(int j=1; j<=col; j++) {
                sums[i][j] = matrix[i-1][j-1] + 
                             sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] ;
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return sums[row2+1][col2+1] - sums[row2+1][col1] - sums[row1][col2+1] + sums[row1][col1];
    }
};

"""
