class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Method 1
        # uppers = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # i = len(s) - 1
        # column = 0
        # while i >= 0:
        #     pos = len(s) - 1 - i
        #     column = column + uppers.index(s[i]) * 26 ** pos
        #     i -= 1
        # return column
        
        # Method 2
        column = 0
        for c in s:
            column = column * 26 + ord(c) - 64
        return column
        
