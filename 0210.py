class Solution(object):
    def findOrder(self, N, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Method 1: BFS: detect zeroDegree
        #child = collections.defaultdict(list)
        #indegree = collections.defaultdict(int)
        #path = []
        #
        #for c, p in prerequisites:
        #    child[p].append(c)
        #    indegree[c] += 1 
        #
        #course = range(N)
        #zeroDegree = True
        #i = 0
        #while zeroDegree and i<N:
        #    zeroDegree = False
        #    for j in course:
        #        if indegree[j] == 0:
        #            zeroDegree = True
        #            break
        #    if not zeroDegree: return []
        #    indegree[j] = -1
        #    course.remove(j)
        #    path.append(j)
        #    for node in child[j]:
        #        indegree[node] -= 1
        #    i += 1
        #return path
        
        # Method 2: DFS: detect loop
        parent = collections.defaultdict(list)
        visited = [0] * N
        path = []
        for c, p in prerequisites:
            parent[c].append(p)
        
        for i in range(N):
            if not self.dfs(parent, visited, path, i):
                return []
        return path
    
    def dfs(self, parent, visited, path, i):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        
        visited[i] = 1
        for p in parent[i]:
            if not self.dfs(parent, visited, path, p):
                return False
        visited[i] = 2
        path.append(i)
        return True
        
               
                
