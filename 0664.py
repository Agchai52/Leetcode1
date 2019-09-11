class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        # Method: recursion dp, huahua https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-664-strange-printer/
        if not s: return 0
        if len(s) == 1: return 1
        
        s = list(s)
        l = len(s)
        self.temp = [[0]*l for _ in xrange(l)]
        return self.turn(s, 0, l-1)
    
    def turn(self, s, i, j):
        if i > j: return 0
        if i == j: return 1
        if self.temp[i][j] > 0: return self.temp[i][j]
        
        ans = self.turn(s, i, j-1) + 1
        for k in range(i, j):
            if s[k] == s[j]:
                ans = min(ans, self.turn(s, i, k)+self.turn(s, k+1, j-1))
        
        self.temp[i][j] = ans
        return self.temp[i][j]
        '''
        
    
        # Method 2: dp
        if not s: return 0
        if len(s) == 1: return 1
        
        s = list(s)
        l = len(s)
        dp = [[0]*(l+1) for _ in xrange(l+1)]
        
        for x in range(1,l+1):
            for y in range(1,x+1):
                dp[y][x] = x - y + 1
                for z in range(y,x):
                    if s[z-1] == s[x-1]:
                        temp = 0
                    else:
                        temp = 1
                    dp[y][x] = min(dp[y][x], dp[y][z-1]+dp[z][x-1]+temp)
        return dp[1][l]
        
            
        
