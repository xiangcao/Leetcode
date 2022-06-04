class Solution(object):
    def findItinerary1(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        self.visitBitmap = {}

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort()
            self.visitBitmap[origin] = [False]*len(itinerary)

        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)

        return self.result


    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                # mark the visit before the next recursion
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True

        return False

    #Approach 2: Hierholzer's Algorithm
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination
            itinerary.sort(reverse=True)

        self.result = collections.deque([])
        self.DFS('JFK')

        # reconstruct the route backwards
        return list(self.result)

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.appendleft(origin)
    
"""
mathematic proof of Hierholzer's algorithm
Here is some mathematical proof of the correctness of the second approach: Hierholzer's Algorithm. The proof is based on the property that an Eularian path, if exists, is one of the dfs search paths before hitting a stuck point. It validates this postorder-like dfs search algo. The follow-up offers an algorithm to deal with the situation where the existence of Eularian path is unknown. Hope the idea is easy to follow!

Lemma:
If the Eularian path exists for this given starting point, the stuck point is guaranteed to be the final vertex in the output itenerary. First, existence of Eularian path necessarily means that the initial stuck point is unique. Furthermore, this intial stuck point is the end point of the Eularian path.

Proof:
A stuck point is, in a dfs search, the point that has no unvisited outgoing edges.
By Def. of Eularian path (the path that traverses all vertices once), an Eularian path is one of the possible dfs search paths before hitting a stuck point (where backtracking comes next). If there were two possible stuck points in dfs search, then Eularian path as a dfs search paths before hitting a stuck point would not be able to cover every edge once. So Eularian path would not exist.
So if Eularian path exists, then there is only one unique stuck point. Since, by Def., Eularian path is a dfs search path that hits this stuck point last, and covers every edge, so this stuck point is the end of the Eularian path. Conversely, by Def., the end of an Eularian path is a dfs stuck point.
After adding the stuck point and removing the last edge, there still exist Eularian path so the proof is still valid. So the next stuck (backtracking) point is also unique and the end point of the Eularian path. Inductively it works at any step. #

After adding the stuck point and removing the last edge, dfs backtracks to a parent point. This point is the end point of the remaining Eularian path, thus is a new stuck point in the resumed dfs search (euquivalent to dfs search from beginning on a graph with the last edge removed). So it will be the next to output and is parent point to the last output point, connected by the last removed edge. So, if Eularian path exist, the output points of this dfs+backtracking algo remain connected, ie the two adjacent output points are also neighboring points in the graph. In other word, if the outputs point are not connect, then the Eularian path does not exists.

Follow up:
Do not know if Eularian path exists. If the output of the dfs+backtracking algo. remains connected, then Eularian path exists and this output is a valid one.

Proof: If Eularian path not exists, then there is at least two stuck points in dfs search. After output one of them and its branch, and removing the edges in the branch, at certain point, the Eularian path re-exists in the remaining graph. At this point, the second stuck point will be the next to output by the algo, but it cannot be an preceding point to the current output suffix path, since the second point belongs to the second branch. (Otherwise there would be only one branch, thus one stuck point in the first place.) Thus the output would not remain connected. #

Therefore, output of the algorithm remains connected if and only if the Eularian path exists. By checking if the stuck point is the parent point of the last output through the last removed edge, the algo can judge if Eularian exists, starting from a given vertex.
"""
