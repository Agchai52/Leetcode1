class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Method 1: BFS
        if not grid or len(grid) == 0: return -1
        m, n = len(grid), len(grid[0])
        flag = 0
        count = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    q = [(i*n+j, 0)]
                    res = float('inf')
                    while len(q) != 0:
                        loc, val = q.pop(0)
                        for x, y in [[0, 1],[0, -1],[1, 0],[-1,0]]:           
                            loc_row = loc / n + x
                            loc_col = loc % n + y                            
                            if loc_row < 0 or loc_row >= m or loc_col < 0 or loc_col >= n or grid[loc_row][loc_col] != flag:
                                continue
                        
                            count[loc_row][loc_col] += 1 + val
                            grid[loc_row][loc_col] -= 1
                            res = min(res, count[loc_row][loc_col])
                            q.append((loc_row*n + loc_col, val+1))
                    flag -= 1
        
        #res = float('inf')
        #for i in xrange(m):
        #    for j in xrange(n):
        #        if grid[i][j] == flag:
        #            res = min(res, count[i][j])
                
        return res if res != float('inf') else -1 
                            
                            
                                
                            
