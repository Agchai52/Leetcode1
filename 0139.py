class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        len_s = len(s)
        dp = [False] * (len_s + 1)
        dp[0] = True
        
        for i in xrange(1, len_s + 1):
            for word in wordDict:
                len_w = len(word)
                if i >= len_w and dp[i-len_w] and word == s[i-len_w:i]:
                    dp[i] = True
                    break
        return dp[-1]
