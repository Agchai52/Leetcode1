class Solution(object):
    def uniquePathsWithObstacles(self, dp):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if dp[0][0] == 1 or dp[-1][-1] == 1:
            return 0
        
        n, m = len(dp[0]), len(dp)
        
        flag = 0
  
        for i in xrange(m):
            for j in xrange(n):
                if dp[i][j] == 1:
                    
                    dp[i][j] = 0
                    if i == 0:
                        flag = 1
                    elif j == 0:
                        flag = 2
                else:
                    if i == 0 or j == 0:
                        if i == 0 and flag == 1:
                            dp[i][j] = 0
                        elif j == 0 and flag == 2:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = 1 
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]   
        
       
        return dp[m-1][n-1]
        
        
