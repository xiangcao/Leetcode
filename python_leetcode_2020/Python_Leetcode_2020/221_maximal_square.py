Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

# DP
Time complexity : O(mn)O(mn). Single pass.

Space complexity : O(mn)O(mn). Another matrix of same size is used for dp.
public class Solution {
    public int maximalSquare(char[][] matrix) {
        int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
        int[][] dp = new int[rows + 1][cols + 1];
        int maxsqlen = 0;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (matrix[i-1][j-1] == '1'){
                    dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1;
                    maxsqlen = Math.max(maxsqlen, dp[i][j]);
                }
            }
        }
        return maxsqlen * maxsqlen;
    }

}

"""
For all people wondering how you'd solve this in an interview in 30 mins - this is a fairly easy DP problem. If you're confused its because the explanation jumps into the bottom-up DP solution without explaining how it got there. You can never figure out a bottom-up DP solution without first figuring out a top down recursive approach. If during the recursion you find you're solving the same sub-problem repeatedly ("overlapping sub-problems") - that's the first hint that its DP. Next, if you find that the optimal answer for the current sub-problem is formed from the optimal answer for the overlapping sub-problems, you now have found the optimal sub-structure. Its DP for sure. Typically problems involving finding the "longest/shortest/largest/smallest/maximal" of something have the optimal-substructure. For example if the shortest distance from A to D is A->B->C->D, then it follows that the shortest distance from B to D is B->C->D.

At first sight, this problem requires a DFS traversal - a dead giveaway that we need recursion. And it also wants you to find the largest square. So you'd go to the first 1 and ask it, "Hey, what's the largest square of 1s that begins with you?". To calculate that it needs to know the largest squares its adjacent cells can begin. So, it'll ask the same question to its adjacent cells which will in turn will ask their adjacent cells and so on... The cell that began the question will deduce that the largest square that begins with it is 1 + the minimum of all the values its adjacent cells returned.

You'd then ask the same question to every 1 you find in the grid and keep track of the global maximum. In doing so, you'll notice that the recursion causes many cells to be asked the same question again and again (overlapping sub-problems)- so you'd use memoization.

The recursive solution takes O(m+n) space. From this, you can now figure out the bottom-up approach.

Recursive solution
    int recursive(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        
        // Add padding to avoid checking for boundary in helper()
        for(auto &v : matrix) v.push_back('0');
        matrix.push_back(vector<char>(matrix[0].size(), '0'));
        
        int res = 0;
        for(int i = 0; i < matrix.size(); ++i) {
            for(int j = 0; j < matrix[0].size(); ++j) {
                res = max(res, helper(matrix, i, j));
            }
        }
        return res * res;
    }
    
    // Return the area of maximum square with (i, j) as upper-left corner.
    int helper(vector<vector<char>>& matrix, int i, int j) {
        if (matrix[i][j] == '0') return 0;
        return min(min(helper(matrix, i, j+1), helper(matrix, i+1, j)), 
                   helper(matrix, i+1, j+1)) + 1;
    }


# Brute force
Approach #1 Brute Force [Accepted]
The simplest approach consists of trying to find out every possible square of 1’s that can be formed from within the matrix. The question now is – how to go for it?

We use a variable to contain the size of the largest square found so far and another variable to store the size of the current, both initialized to 0. Starting from the left uppermost point in the matrix, we search for a 1. No operation needs to be done for a 0. Whenever a 1 is found, we try to find out the largest square that can be formed including that 1. For this, we move diagonally (right and downwards), i.e. we increment the row index and column index temporarily and then check whether all the elements of that row and column are 1 or not. If all the elements happen to be 1, we move diagonally further as previously. If even one element turns out to be 0, we stop this diagonal movement and update the size of the largest square. Now we, continue the traversal of the matrix from the element next to the initial 1 found, till all the elements of the matrix have been traversed.

Java

public class Solution {
    public int maximalSquare(char[][] matrix) {
        int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
        int maxsqlen = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == '1') {
                    int sqlen = 1;
                    boolean flag = true;
                    while (sqlen + i < rows && sqlen + j < cols && flag) {
                        for (int k = j; k <= sqlen + j; k++) {
                            if (matrix[i + sqlen][k] == '0') {
                                flag = false;
                                break;
                            }
                        }
                        for (int k = i; k <= sqlen + i; k++) {
                            if (matrix[k][j + sqlen] == '0') {
                                flag = false;
                                break;
                            }
                        }
                        if (flag)
                            sqlen++;
                    }
                    if (maxsqlen < sqlen) {
                        maxsqlen = sqlen;
                    }
                }
            }
        }
        return maxsqlen * maxsqlen;
    }
}
Complexity Analysis

Time complexity : O\big((mn)^2\big)O((mn) 
2
 ). In worst case, we need to traverse the complete matrix for every 1.
Space complexity : O(1)O(1). No extra space is used.
