class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        '''
        0. visited = [False]m * n, each loc if it is visited 
        1. two loops and visited: detect loc of 0 O(MN) save it into a 
        2. for 4 directions up down left right, set them to zeros O(MN)
        3. dfs: keep one direction, set zeors until touch boundry 
        '''
        if not matrix or not matrix[0]: return 
        m, n = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        zeros_row = set()
        zeros_col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    continue
                zeros_row.add(i)
                zeros_col.add(j)
        
        for i in zeros_row:
            matrix[i] = [0]*n
        
        for j in zeros_col:
            for i in range(m):
                matrix[i][j] = 0
            
                    
