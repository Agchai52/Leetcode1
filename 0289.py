class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Method Bit: last 1st and 2nd of bit 
        m = len(board)
        n = len(board[0])
        
        for i in xrange(m):
            for j in xrange(n):
                live = 0
                # 3x3 including cell
                for x in xrange(max(0, i-1), min(m, i+2)):
                    for y in xrange(max(0, j-1), min(n, j+2)):
                        live += board[x][y] & 1 # only consider last bit since it's current and the last second represents next generation
                if live == 3 or live - board[i][j] == 3:
                    board[i][j] |= 0b10 
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
                
