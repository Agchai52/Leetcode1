class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Method 1
        #return map(s.find, s) == map(t.find, t)  
        
        # Method 2
        letters = {}
        pos = {}
        for i in xrange(len(s)):
            if s[i] in letters:
                if letters[s[i]] != t[i]:
                    return False
            elif t[i] in pos:
                return False
            else:
                letters[s[i]] = t[i]
                pos[t[i]] = True
        return True
