class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        '''
        1. egdge case: 0, 1
        2. dp or iteration
        '''
        '''
         # Method: Recursion O(2^N)
        if N == 0: return 0
        if N == 1 or N == 2: return 1
        return self.fib(N-1) + self.fib(N-2)
        '''
        '''
        # Method: dp O(N)
        if N == 0: return 0
        if N == 1 or N == 2: return 1
        
        dp = [0] * (N+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for i in xrange(3, N+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[N]
        '''
        # Method: O(N)
        if N == 0: return 0
        if N == 1 or N == 2: return 1
        pre = 1
        cur = 1
        i = 3
        while i <= N:
            temp = cur            
            cur = pre + cur
            pre = temp
            i += 1
        return cur
        
       
