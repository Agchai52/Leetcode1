class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # Method 1: DFS
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        res = 1
        cache = [[-1]*n for _ in xrange(m)] # -1: not visited, max_path
        for i in range(m):
            for j in range(n):
                path = self.dfs(matrix, cache, m, n, i, j)
                res = max(res, path)
        return res
    
    def dfs(self, matrix, cache, m, n, i, j):
        if cache[i][j] != -1:
            return cache[i][j]
        res = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            x, y = i+d[0], j+d[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[i][j] >= matrix[x][y]:
                continue
            path = 1 + self.dfs(matrix, cache, m, n, x, y)
            res = max(res, path)
        cache[i][j] = res
        return res
