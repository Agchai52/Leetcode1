class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        if len(s) == 1: return 1
        max_size = 1
        start, end = 0, 1
        chars = [s[0]]
        
        while end < len(s):
            if s[end] in chars:                
                chars.remove(s[start])
                start += 1
            else:
                chars.append(s[end])
                end += 1
                max_size = max(max_size, end-start)           
        return max_size
