class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Method 1:
        '''
        if not s: return s
        
        buff = ''
        res = ''
        for i in range(len(s)):
            c = s[i]
            if c == ' ' or i == len(s)-1:
                if i == len(s)-1:
                    buff += c   
                res += buff[::-1]
                if i!= len(s)-1:
                    res += ' '
                buff = ''
            else:
                buff += c
        return res
        '''
        # Method 2
        if not s: return s
        list_s = s.split(' ')
        res = ''
        for w in list_s:
            res += w[::-1] + ' '
        return res[:-1]
                
            
