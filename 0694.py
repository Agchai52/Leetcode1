class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        shapes = []
        
        def process(shape):
            row = []
            mr = float('inf')
            mc = float('inf')
            for (i, j) in shape:
                row.append(i)
                mr = min(mr, i)
            for i in xrange(len(row)):
                if row[i] == mr:
                    mc = min(mc, shape[i][1])            
            #print(mr,mc)
        
            for k in xrange(len(shape)):
                shape[k][0] = shape[k][0] - mr
                shape[k][1] = shape[k][1] - mc
            
            shape.sort()
            return shape
        
        def countPath(shapes):
            res = 0
            unique = []
            for shape in shapes:
                if not shape:
                    continue
                newShape = process(shape)
                if newShape not in unique:
                    unique.append(newShape)
            #print(unique)
            return len(unique)            
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] != 1:
                    continue
                grid[i][j] = -1
                path = [[i,j]]
                self.dfs(grid, m, n, i, j, path)
                shapes.append(path)
        #print(grid)
        #print(shapes)
        return countPath(shapes)
    
    def dfs(self, grid, m, n, i, j, path):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                continue
            grid[x][y] = -1
            path.append([x, y])
            self.dfs(grid, m, n, x, y, path)
        
        
