class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        d = collections.Counter(s)
        extra = 0
        for k in d:
            if d[k] % 2 == 1:
                extra += 1
        if extra == 0: return n
        else: return n-extra+1

    
