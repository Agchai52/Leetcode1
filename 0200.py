class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        '''
        Method DFS
        1. if grid[i][j] == 1, dfs explore all neighbors == -1 and mark it -1
        2. res += 1
        '''
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] != '1':
                    continue  
                res += 1
                self.dfs(grid, m, n, i, j)
        return res
    
    def dfs(self, grid, m, n, i, j):
        grid[i][j] = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != '1':
                continue            
            self.dfs(grid, m, n, x, y)
            
'''
grid = [[-1,0],
        [-1, 0],
        [0, 1]]
island = 2

m = 3
n = 2
grid[1][1]

'''
