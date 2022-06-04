"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        visited = [False] * numCourses
        path = [False] * numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, path, visited):
                return False
        return True


    def isCyclic(self, currCourse, courseDict, path, visited):
        """
        backtracking method to check that no cycle would be formed starting from currCourse
        """
        # 1). bottom-cases
        if visited[currCourse]:
            # this node has been checked, no cycle would be formed with this node.
            return False
        
        if path[currCourse]:
            # came across a marked node in the path, i.e. detect the cycle
            return True

        # before backtracking, mark the node in the path
        path[currCourse] = True

        # backtracking
        for child in courseDict[currCourse]:
            if self.isCyclic(child, courseDict, path, visited):
                return True

        # after backtracking, remove the node from the path
        path[currCourse] = False
        visited[currCourse] = True
        return False
        
