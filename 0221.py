class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # dp[i][j]: the biggest edge of upper-left squre of (i,j) including itself
        dp = [[0]*n for _ in xrange(m)]
        
        for row in xrange(0, m):
            for col in xrange(0, n):
                if row == 0 or col == 0:
                    dp[row][col] = int(matrix[row][col]) 
                else:
                    if int(matrix[row][col]) == 1:
                        dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                            
                    
        return max(map(max,dp))**2
                
