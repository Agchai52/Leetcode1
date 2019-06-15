class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 3 Methods in total: DP, Recursion, Space Compression
        
        # Method 1: DP
        #dp = [0] * (n+1)
        #dp[0] = 1
        #dp[1] = 1
        #for i in xrange(2, n+1):
        #    dp[i] = dp[i-1] + dp[i-2]
        #return dp[-1]
        
        # Method 2: Space Compression
        if n == 1:
            return 1
        first, second = 1, 2
        for i in xrange(3, n+1):
            third = first + second
            first = second
            second = third
        return second
