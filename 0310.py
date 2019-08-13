class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        leaves = collections.defaultdict(set)
        que = []
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
        for u, vs in leaves.items():
            if len(vs) == 1:
                que.append(u)
        
        while n > 2:
            _len = len(que)
            n -= _len
            
            for _ in xrange(_len):
                u = que.pop(0)
                for v in leaves[u]:
                    leaves[v].remove(u)
                    if len(leaves[v]) == 1:
                        que.append(v)
        return que
        
        
