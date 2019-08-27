import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        '''
        s = abcab, n = 5
        p = abc, k = 3
        i = [0,1,2,3)
        '''
        # Method 1: continuous and with same length TLE
        #if len(s) < len(p): return []
        #n = len(s)
        #k = len(p)
        #key = collections.Counter(p)
        #res = []
        #for i in range(0, n-k+1):
        #    
        #    if collections.Counter(s[i:i+k]) == key:
        #        res.append(i)
        #return res
    
        # Method 2: Sliding Window
        if len(s) < len(p): return []
        n = len(s)
        k = len(p)
        res = []
        cp = collections.Counter(p)
        cs = collections.Counter(s[:k-1])
        for i in range(k-1, n):
            cs[s[i]] += 1
            if cs == cp:
                res.append(i-k+1)
            cs[s[i-k+1]] -= 1
            if cs[s[i-k+1]] == 0:
                del cs[s[i-k+1]]
        return res
            
