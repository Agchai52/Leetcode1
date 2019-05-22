class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = [c for c in s.lower() if c.isalnum()]
        return chars == chars[::-1]
