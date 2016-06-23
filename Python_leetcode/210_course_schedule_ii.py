class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited=[0 for i in range(numCourses)]
        adjlist = [set() for i in range(numCourses)]
        result=[]
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
            result.append(root)
            return True
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return result[::-1]
        
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree=[0 for i in range(numCourses)]
        adjlist = [set() for i in range(numCourses)]
        result=[]
        for edge in prerequisites:
            adjlist[edge[1]].add(edge[0])
        for node in range(numCourses):
            for nbor in adjlist[node]:
                indegree[nbor] += 1
        queue=[i for i in range(numCourses) if indegree[i] == 0 ]
        
        while queue:
            cur = queue.pop()
            result.append(cur)
            for nbor in adjlist[cur]:
                indegree[nbor] -= 1
                if indegree[nbor] == 0:
                    queue.append(nbor)
        return result if len(result) == numCourses else []
