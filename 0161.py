class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Method 1: Brute Force
        #len_s = len(s)
        #len_t = len(t)
        #if abs(len_s - len_t) > 1:
        #    return False
        #if s == t:
        #    return False
        #if abs(len_s - len_t) == 1:
        #    if len_s < len_t:
        #        i = 0
        #        while i < len_s:
        #            if s[i] != t[i]:
        #                t = t[:i]+t[i+1:]
        #                return s == t
        #            i += 1
        #        t = t[:-1] 
        #        return s == t
        #    else:
        #        i = 0
        #        while i < len_t:
        #            if s[i] != t[i]:
        #                s = s[:i]+s[i+1:]
        #                return s == t
        #            i += 1
        #        s = s[:-1] 
        #        return s == t
        #            
        #elif abs(len_s - len_t) == 0:
        #    i = 0
        #    while i < len_s:
        #        if s[i] != t[i]:
        #            s = s[:i]+s[i+1:]
        #            t = t[:i]+t[i+1:]
        #            return s == t
        #        i += 1
        #    return False
        
        # Method 2: Brute Force
        # len_s = len(s)
        # len_t = len(t)
        # if abs(len_s - len_t) > 1:
        #     return False
        # if s == t:
        #     return False
        # for i in xrange(min(len_s, len_t)):
        #     if s[i] != t[i]:
        #         if len_s == len_t:
        #             return s[i+1:] == t[i+1:]
        #         elif len_s < len_t:
        #             return s[i:] == t[i+1:]
        #         elif len_s > len_t:
        #             return s[i+1:] == t[i:]
        # return abs(len_s - len_t) == 1
        
        ## Method 3: https://www.cnblogs.com/lightwindy/p/8606871.html
        #len_s = len(s)
        #len_t = len(t)
        #if abs(len_s - len_t) > 1:
        #    return False
        #if s == t:
        #    return False

'''
if __name__ == '__main__':
    s = '1203'
    t = '1213'
    print(Solution().isOneEditDistance(s,t))
'''            
