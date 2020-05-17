class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N = len(matrix), len(matrix[0])       
        if M == 0 or N == 0: return matrix
        visited = set()
        q = []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        
        while q:
            r, c = q.pop(0)
            for dx, dy in dirs:
                x, y = r + dx, c + dy
                if (0 <= x < M and 0 <= y < N and (x, y) not in visited):
                    matrix[x][y] = matrix[r][c] + 1
                    visited.add((x, y))
                    q.append((x, y))
                
        
        return matrix
                                
                            
                                
                                
                        
                         
                         
        
