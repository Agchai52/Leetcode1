class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        '''
        board: [[X,.,.],
                [X,.,X],
                [X,.,.]]
        1. m, n
        2. 0
        '''
        # Method 1: Bruth Force
        if not board: return 0
        
        m = len(board)
        n = len(board[0])
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == 'X':
                        continue
                    if j > 0 and board[i][j-1] == 'X':
                        continue
                    count += 1
        return count

#if __name__ == '__main__':
#    board = [['X','.','.'],['X','X','X'], ['X','.','.']]
#    res = Solution().countBattleships(board)
#    print(res)
        
        
