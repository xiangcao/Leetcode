class Solution(object):
    
    #time limit exceeded
    #correct
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        result = []
        
        def find(curDepart, remainingTickets, curItinerary):
            if not remainingTickets:
                result.append(curItinerary)
                return 
            for i, t in enumerate(remainingTickets): # iterating over possible destination city from curDepart
                if t[0] == curDepart:
                    find(t[1], remainingTickets[:i]+remainingTickets[i+1:], curItinerary+[t[1]])
        
        find("JFK", tickets, ["JFK"])
        
        
        result.sort(key=lambda x: ''.join(x))
        if not result:
            return []
        return result[0]
    
        
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        
        dest = collections.defaultdict(list)
        for flight in tickets:
            dest[flight[0]] += flight[1],
        
        def find(curDepart, curItinerary):
            if len(curItinerary) == len(tickets)+1:
                return curItinerary
            #dest[curDepart].sort()
            #for d in dest[curDepart]:
            destList = sorted(dest[curDepart])
            
            for d in destList: # iterating over possible destination city from curDepart
                dest[curDepart].remove(d)
                result = find(d,  curItinerary+[d])
                if result:
                    return result
                dest[curDepart].append(d)
        
        result = find("JFK", ["JFK"])
        return result
        
        result.sort(key=lambda x: ''.join(x))
        if not result:
            return []
        return result[0]
    
        
    """  
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)
        for flight in tickets:
            d[flight[0]] += flight[1],
        self.route = ["JFK"]
        def dfs(start = 'JFK'):
            if len(self.route) == len(tickets) + 1:
                return self.route
            myDsts = sorted(d[start])
            for dst in myDsts:
                d[start].remove(dst)
                self.route += dst,
                worked = dfs(dst)
                if worked:
                    return worked
                self.route.pop()
                d[start] += dst,
        return dfs()
    """


sol = Solution()

tickets=[["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]

result = sol.findItinerary(tickets)
print result

