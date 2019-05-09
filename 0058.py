class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for i in s.strip():
            if i == ' ':
                a = 0
            else:
                a += 1
        return a
        
