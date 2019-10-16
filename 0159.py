class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
         0123456
        "abaccc"
         l
          r
        htalbe = 
        res = 
        
        '''
        if len(s) <= 2: return len(s)
        res = 0
        l, r = 0, 1
        htable = collections.defaultdict(int)
        htable[s[0]] += 1
        while r < len(s):
            char = s[r]
            htable[char] += 1
            while len(set(htable)) > 2 and l < r:
                if s[l] in htable:
                    htable[s[l]] -= 1
                    if htable[s[l]] == 0:
                        del htable[s[l]]
                l += 1
               
            res = max(res, r-l+1)
            r += 1
        return res
            
        
        
