class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        1. odd exists, delet one
        2. only even, but wong loc
        '''
        # Method 1: Brute Force TLE
        # if not s: return False
        # if self.isValid(s): return True
        # n = len(s)
        # for i in range(n):
        #     if self.isValid(s[:i]+s[i+1:]): 
        #         return True        
        # return False
        
        # Method 2: Two pointers https://blog.csdn.net/fuxuemingzhu/article/details/79252779
        if not s: return False
        n = len(s)
        l, r = 0, n-1
        while l <= r:
            if s[l] != s[r]:
                return self.isValid(s[:l]+s[l+1:]) or self.isValid(s[:r]+s[r+1:])
            l += 1
            r -= 1
        return True
    def isValid(self, s):
        n = len(s)
        for i in xrange((n)/2):
            if s[i] != s[n-i-1]:
                return False
        return True
