class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs: return 0
        if len(pairs) == 1: return 1
        n = len(pairs)
        
        # Method 1: DP + Brute Force almost TLE, global optimal
        #pairs.sort(lambda x, y: x[0]-y[0] if x[0]!=y[0] else y[1]-x[1])
        #dp = [1] * n
        #for i in range(n):
        #    for j in range(i):
        #        if pairs[j][1] < pairs[i][0]:
        #            dp[i] = max(dp[i], dp[j]+1)
        #            
        #return max(dp)
        
        # Method 2: Greedy, every step is optimal
        pairs.sort(key = lambda x:x[1])
        pre = float('-inf')
        res = 0
        for x, y in pairs:
            if x > pre:
                res += 1
                pre = y
        return res
                    
