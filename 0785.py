class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # Method 1: Color Graph using BFS
        #''' 
        #node    : [0(1),     1(-1),     2(1),     3(-1)]
        #neighbor: [[1(-1),3(-1)], [0(1),2(1)], [1(-1),3(-1)], [0(1),2(1)]]
        #'''
        #l = len(graph)
        #visited = [0] * l # 0--not visited, 1--blur, -1--red
        #for i in range(l):
        #    if graph[i] and visited[i] == 0:
        #        visited[i] = 1
        #        q = [i]
        #        while q:
        #            node = q.pop(0)
        #            for val in graph[node]:
        #                if visited[val] == 0:
        #                    visited[val] = -visited[node]
        #                    q.append(val)
        #                else:
        #                    if visited[val] == visited[node]:
        #                        return False
        #return True
        
        # Method 2: Color Graph using DFS
        '''
        node: [0,1,2,3]
        neighbor: [[1,3], [0,2], [1,3], [0,2]]
        '''
        l = len(graph)
        visited = [0]*l
        for i in range(l):
            if visited[i] == 0 and not self.valid(graph, 1, i , visited):
                return False
        return True
    
    def valid(self, graph, color, node, visited):
        if visited[node] != 0: 
            return visited[node] == color
        visited[node] = color
        for nei in graph[node]:
            if not self.valid(graph, -color, nei, visited): 
                return False
        return True
