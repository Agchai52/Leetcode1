class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Method 1
        #return sorted(s) == sorted(t)
        
        # Method 2
        if len(s) != len(t):
            return False
        alpha  = {}
        beta = {}
        for c in s:
            alpha[c] = alpha.get(c, 0) + 1
        for c in t:
            beta[c] = beta.get(c, 0) + 1
        return alpha == beta
    
        
