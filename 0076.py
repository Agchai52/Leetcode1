class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Method 1: Sliding Window Time=O(n+k) Space=O(n+k)
        if not s or not t: return ''
        dict_t = collections.Counter(t)
        required = len(dict_t)
        dict_win = dict()
        l, r = 0, 0
        formed = 0
        res = float('inf'), None, None # win_len, left, right
        while r < len(s):
            char = s[r]
            dict_win[char] = dict_win.get(char, 0) + 1
            # if char in t is ok
            if char in dict_t and dict_win[char] == dict_t[char]:
                formed += 1
            # if all chars in t is ok: count length and shrink left
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < res[0]:
                    res = (r-l+1, l, r)
                dict_win[char] -= 1
                if char in dict_t and dict_win[char] < dict_t[char]:
                    formed -= 1
                l += 1
            r += 1
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]
        
        # Method 2: Optimal Sliding Window: find char in filter S
            
