class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Method dp: https://blog.csdn.net/DaVinciL/article/details/99545037
        row, col = len(text1) + 1, len(text2) + 1
        # dp[i][j] max len of common for t1[:i+1] and t2[:j+1]
        dp = [[0] * col for _ in range(row)]
        
        for i in range(1, row):
            for j in range(1, col):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        
