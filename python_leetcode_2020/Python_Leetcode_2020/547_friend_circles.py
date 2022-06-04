"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]

"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, visited, i):
            visited[i] = True
            for j in range(len(M)):
                if (M[i][j] == 1 and i != j and not visited[j]):
                    dfs(M, visited, j)

        visited = [False] * len(M)
        count = 0
        for i in range(len(M)):
            if not visited[i]:
                dfs(M, visited, i)
                count += 1
        return count

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        parent = [-1] * N
        rank = [0] * N 
        def find(i):
            if parent[i] == - 1:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(x, y):
            xParent = find(x)
            yParent = find(y)
            if xParent == yParent:
                return 
            if rank[xParent] == rank[yParent]:
                parent[xParent] = yParent
                rank[yParent] += 1
            elif rank[xParent] > rank[yParent]:
                parent[yParent] = xParent
            else:
                parent[xParent] = yParent

        
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1 and i != j:
                    union(i, j)
                    
        return sum(1 for p in parent if p == -1)
