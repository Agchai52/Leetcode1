class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Method 1
        # s = list(str(x))
        # return s == s[::-1]
        
        # Method 2 
        s = str(x)
        for i in xrange(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
