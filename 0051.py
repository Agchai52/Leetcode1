class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        '''
        1. one Q each col and one Q each row
        2. from top down, locate Q0 -- Qn-1
        3. for each row Qi, check location from col0 -- coln-1 if conflicts
        4. conficts:
           - same col of pre Q
           - diag of pre Q -> vertical Distance == horizantal Distance 
        '''
        def check(Q_id, col):
            '''
            check if current location is valid
            '''
            for j in range(Q_id):
                if board[j] == col or abs(Q_id-j) == abs(board[j]-col):
                    # same col or distance vertical (|Qj-Qi|) == distance horizantal (d = |col[Q_j] - col[Q_i]|)
                    return False
            return True
        
        def dfs(board, Q_id, path, res):
            if Q_id == len(board):
                res.append(path)
            for col in xrange(len(board)):
                if check(Q_id, col):
                    s = '.' * len(board)
                    board[Q_id] = col
                    dfs(board, Q_id+1, path + [s[:col]+'Q'+s[col+1:]], res)
        
        board = [-1 for i in xrange(n)]
        res = []
        path = []
        dfs(board, 0, path, res)
        return res
