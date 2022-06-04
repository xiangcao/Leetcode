# bfs
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph=collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        def process(wordA, wordB):
            lenA, lenB = len(wordA), len(wordB)
            for i in range(min(lenA, lenB)):
                if wordA[i] == wordB[i]:
                    continue
                else:
                    if (wordB[i] not in graph[wordA[i]]):
                        graph[wordA[i]].add(wordB[i])
                        indegree[wordB[i]] += 1
                    return True
            return lenA <= lenB

        numOfWords = len(words)
        """
        can simplify the loops below into 
        for i in range(numOfWords-1):
            if not process(words[i], words[i+1]):
                return ""
        """

        for i in range(numOfWords-1):
            for j in range(i+1, numOfWords):
                if not process(words[i], words[j]):
                    return ""
        
        def topologicalSort(graph):
            queue = collections.deque()
            allNodes = set(''.join(words))
            
            for node in allNodes:
                if indegree[node] == 0:
                    queue.append(node)
            orderedList = []
            while queue:
                node = queue.popleft()
                orderedList.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            if len(allNodes) != len(orderedList):
                return []
            return orderedList
        return "".join(topologicalSort(graph))
                
                

# dfs
