class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        # board[i][j] == 'E'
        # count mines in eighbor
        neighbor = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        m,  n = len(board), len(board[0])
        count = self.dfs(board, m, n, i, j)        
        board[i][j] = self.Mark(count)
        if count == 0:
            for nei in neighbor:
                x, y = i + nei[0], j + nei[1]
                if x<0 or x>=m or y<0 or y>=n or board[x][y]!='E':
                    continue
                self.updateBoard(board, [x,y])
                                    
        return board
    
    def Mark(self, count):
        if count == 0:
            mark = 'B'
        else:
            mark = str(count)
        return mark
        
    
    # count neighbor of i,j
    def dfs(self, board, m, n, i, j):
        neighbor = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for nei in neighbor:
            x, y = i + nei[0], j + nei[1]
            if 0<=x<m and 0<=y<n:              
                if board[x][y] == 'M' or board[x][y] == 'X':
                    count += 1
        return count
                
                
        
