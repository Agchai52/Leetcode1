class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
    # Method 1: Bit Manipulation
    #    if k == 1: return len(s)
    #    res = 0
    #    n = len(s)
    #    i = 0
    #    while i + k <= n:
    #        mask = 0
    #        max_idx = i
    #        m = [0] * 26
    #        for j in xrange(i, n):
    #            t = ord(s[j]) - ord('a')
    #            m[t] += 1
    #            if m[t] < k:               # mask: 0 >= k, 1 < k
    #                mask |= 1 << t
    #            else:
    #                mask &= ~(1 << t)
    #            if mask == 0:
    #                res = max(res, j - i + 1)
    #                max_idx = j
    #        i = max_idx + 1
    #    return res
                
    
                
                
                
            
