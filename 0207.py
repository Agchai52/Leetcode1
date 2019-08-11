class Solution(object):
    def canFinish(self, N, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Method 1: DFS
   #     graph = collections.defaultdict(list)
   #     for u, v in prerequisites:
   #         graph[u].append(v)
   #     # 0 = Unknown, 1 = visiting, 2 = visited
   #     visited = [0] * N
   #     for i in range(N):
   #         if not self.dfs(graph, visited, i):
   #             return False
   #     return True
   #     
   # # Can we add node i to visited successfully?
   # def dfs(self, graph, visited, i):
   #     if visited[i] == 1: return False
   #     if visited[i] == 2: return True
   #     visited[i] = 1
   #     for j in graph[i]:
   #         if not self.dfs(graph, visited, j):
   #             return False
   #     visited[i] = 2
   #     return True
    
        # Method 2: BFS
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegree[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegree[j] = -1
            for node in graph[j]:
                indegree[node] -= 1
        return True
        
