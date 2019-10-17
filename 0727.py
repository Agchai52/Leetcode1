class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        '''
        https://www.cnblogs.com/lightwindy/p/8486724.html
        # Method 1: left to right
        if not S or not T: return ''
        # dp[i][j] index of S , where S[index:j] include T[0:i]
        dp = [[None for _ in range(len(S))] for _ in range(2)]
        
        # find start (T[0]) of T in S
        for j, c in enumerate(S):
            if c == T[0]:
                dp[0][j] = j
        
        # dp[i%2], row i%2, 0,1,0,1..., since only need 2 rows in total 
        for i in range(1, len(T)):
            prev = None
            dp[i%2] = [None] * len(S)
            for j, c in enumerate(S):
                if prev is not None and c == T[i]:
                    dp[i%2][j] = prev
                if dp[(i-1)%2][j] is not None:
                    prev = dp[(i-1)%2][j]
        
        start, end = 0, len(S)
        # if last row has index, find the min len 
        for j, i in enumerate(dp[(len(T)-1)%2]):
            if i >= 0 and j - i < end - start:
                start, end = i, j
        return S[start:end+1] if end < len(S) else ''
        '''
        
        # Method 2: right to left
        '''
        dp[y]: i in S and S[i] == T[0]
             012345678
        S = 'abcdebdde'
                  x
        T = 'bde'
             y
               0  1  2
        dp = [ 5, 1, 1]
        dp[y] = dp[y-1] if y else x
        dp[0] = x = 1
        dp[1] = dp[0] = 1
        dp[2] = dp[1] = 1
        nlen = x - dp[-1] + 1 = 4-1+1 = 4
        ans = ''
        
            012345678
        S ='amcm'
               x
        T ='mm'
             y
               0  1  2
        dp = [ 1,-1]
        dp[y] = dp[y-1] if y else x
        dp[0] = x = 1
        dp[1] = dp[0] = 1
        
        nlen = x - dp[-1] + 1 = 4-1+1 = 4
        '''
        
        ans = ''
        ls, lt = len(S), len(T)
        dp = [-1] * lt
        for x in range(ls):
            for y in range(lt-1, -1, -1): # cannot use range(lt)
                if T[y] == S[x]:
                    dp[y] = dp[y-1] if y else x
                    if y == lt-1 and dp[-1] > -1:
                        nlen = x - dp[-1] + 1
                        if not ans or nlen < len(ans):
                            ans = S[dp[-1]:x+1]
        return ans
        
            
  
