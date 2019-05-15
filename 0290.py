class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        hashmap = {}
        valmap = {}
        for i in xrange(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != pattern[i]:
                    return False
            elif pattern[i] in valmap:
                return False
            else:
                hashmap[s[i]] = pattern[i]
                valmap[pattern[i]] = True
        return True
