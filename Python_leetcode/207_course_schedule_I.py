"""
http://bookshadow.com/weblog/2015/05/07/leetcode-course-schedule/
https://leetcode.com/discuss/34791/bfs-topological-sort-and-dfs-finding-cycle-by-c


"""

class Solution(object):
    #DFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited=[0 for i in range(numCourses)]
        adjlist = [set() for i in range(numCourses)]
        for edge in prerequisites:
            adjlist[edge[1]].add(edge[0])
        def dfs(root):
            visited[root] = 1 
            for neighbor in adjlist[root]:
                if visited[neighbor] == 1: #cycle
                    return False
                elif  visited[neighbor] == 0:
                    if not dfs(neighbor):
                        return False
            visited[root] = 2
            return True
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True
        
    #BFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        10
        [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
         Output: false
         Expected: true 
         count = 9, numCourses = 10
         """
        indegree=[0 for i in range(numCourses)]
        adjlist = [set() for i in range(numCourses)]
        
        for edge in prerequisites:
            adjlist[edge[1]].add(edge[0])
        for node in range(numCourses):
            for nbor in adjlist[node]:
                indegree[nbor] += 1
        queue=[i for i in range(numCourses) if indegree[i] == 0 ]
        
        count  = 0
        while queue:
            count += 1
            cur = queue.pop()
            for nbor in adjlist[cur]:
                indegree[nbor] -= 1
                if indegree[nbor] == 0:
                    queue.append(nbor)
        print count, numCourses
        return count == numCourses
            
            
