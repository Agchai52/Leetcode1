class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Method 1: HashTable
        #dictS, dictT = collections.Counter(s), collections.Counter(t)
        #for t in dictT:
        #    if dictT[t] > dictS[t]:
        #        return t
        
        # Method 2: Bit Manipulation
        #return chr(reduce(operator.xor, map(ord, s+t)))
        return chr(reduce(lambda x, y: x^y, map(ord, s+t)))
    
        # Method 3:
        res = [ord(t[-1])]
        for i in xrange(len(s)):
            res = res + ord(t[i]) - ord(s[i])
        return chr(res)
