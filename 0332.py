class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        #Method:https://blog.csdn.net/fuxuemingzhu/article/details/83551204
        if len(tickets) == 0: return []
        if len(tickets) == 1: return tickets[0]
        
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
       
        for frm in graph:
            graph[frm].sort() # graph[frm].sort(reverse=True)
        
        res = []
        self.dfs(graph, 'JFK', res)
        return res[::-1]
            
    def dfs(self, graph, frm, res):
        while graph[frm]:
            v = graph[frm].pop(0) # v = graph[frm].pop()
            self.dfs(graph, v, res)
        res.append(frm)
            
            
            
