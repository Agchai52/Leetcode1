class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        dp = [ [0] * (n + 1) for _ in range  (n+1) ]
        for gap in xrange(1, n):
            for lo in xrange(1, n-gap+1):
                hi = lo + gap
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi]) for x in xrange(lo,hi))
        
        return dp[1][n]
