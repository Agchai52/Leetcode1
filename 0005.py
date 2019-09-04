class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1: return s
        n = len(s)
        dp = [[0]*n for _ in xrange(n)]
        start, end, maxL = 0, 0, 0
        for i in xrange(n):
            for j in xrange(i):
                dp[j][i] = (s[i]==s[j]) and ((i == j + 1) or dp[j+1][i-1])
                if dp[j][i] and maxL < i - j + 1:
                    maxL = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start:end+1]
                
