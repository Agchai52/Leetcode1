class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Method 1: DP slow
        dp = [2 ** 32 -1] * (n+1)
        
        dp[0] = 0
        dp[1] = 1
        for i in xrange(2, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]
