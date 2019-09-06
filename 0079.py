class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        '''
        Method: DFS
        same letter multiple? No
        'ABCD'
        1. Traverse matrix find initial
        2. dfs start check its neighbor
        3. dfs(board, word, index, m, n, i, j)
        4. True: index == len(word)
        5. False: 
           - cannot find target in neighbor
           
        6. Trap: no return, not in previous
        '''
        
        if not board and not board[0]: return False
        m, n = len(board), len(board[0])
        if len(word) > m*n: return False      
        
        def dfs(index, m, n, i, j): 
            if index == len(word):
                return True           
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[index]:
                return False
            board[i][j] = board[i][j].swapcase()
            isValid = dfs(index+1, m, n, i+1, j) \
            or dfs(index+1, m, n, i-1, j) \
            or dfs(index+1, m, n, i, j+1) \
            or dfs(index+1, m, n, i, j-1)
            board[i][j] = board[i][j].swapcase()
            return isValid                    
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue             
                if dfs(0, m, n, i, j): 
                    return True              
        return False
