class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Method 1: Sliding Window TLE
        #if k == 0 or len(s) == 0: return 0
        #if k >= len(s): return len(s)
        #longest = float('-inf')
        #l, r = 0, 0
        #while r < len(s):
        #    if r < len(s) and len(set(s[l:r+1])) <= k:
        #        r += 1
        #    longest = max(longest, r-l)
        #    if l <= r and len(set(s[l:r+1])) > k: 
        #        l += 1
        #return longest
        
        # Method 2: Jump to end of first letter in table
        table = {}
        low, res = 0, 0
        for i, c in enumerate(s):
            table[c] = i
            if len(table) > k:
                low = min(table.values())
                del table[s[low]]
                low += 1
            res = max(res, i-low+1)
        return res
