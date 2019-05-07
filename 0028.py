class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        elif needle in haystack:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                           return i
                    
        else:
            return -1
