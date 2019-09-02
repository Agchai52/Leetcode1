class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        color = [0]*N
        # creat graph
        for d in dislikes:
            graph[d[0]-1].append(d[1]-1)
            graph[d[1]-1].append(d[0]-1)
        # color graph
        for n in graph:
            if n and color[n] == 0:
                color[n] = 1
                q = [n]
                while q:
                    node = q.pop(0)
                    for e in graph[node]:
                        if color[e] == 0:
                            color[e] = -color[node]
                            q.append(e)
                        else:
                            if color[e] == color[node]:
                                return False
        return True
                            
