class Solution:
    # DfS
    """
    Time Complexity: O(sum(a_i*log(a_i))), where a_i is the length of accounts[i]. Without the log factor, this is the complexity to build the graph and search for each component. The log factor is for sorting each component at the end.

     Space Complexity: O(∑ai), the space used by our graph and our search.

    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(list)
        emailToUser = {}
        
        for account in accounts:
            user = account[0]
            for i in range(1, len(account)):
                emailToUser[account[i]] = user
                if i == 1:
                    continue
                graph[account[i]].append(account[i-1])
                graph[account[i-1]].append(account[i])
        visited = set()
        result = []
        for email in emailToUser:
            user = emailToUser[email]
            if email not in visited:
                account = []
                visited.add(email)
                self.dfs(graph, email, visited, account)
                account.sort()
                account.insert(0, user)
                result.append(account)
        return result

    def dfs(self, graph, email, visited, account):
        account.append(email)
        for nei in graph[email]:
            if nei not in visited:
                visited.add(nei)
                self.dfs(graph, nei, visited, account)
        

    # method 2: Union Find
