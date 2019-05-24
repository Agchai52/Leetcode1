class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        
        s = s.strip()
        
        if not s:
            return 0
        
        num_s = ''
        flag = 1
        if s[0] == '-':
            s = s[1:]
            flag = -1
        elif s[0] == '+':
            s = s[1:]
        for c in s:
            if c in '0123456789':
                num_s += c
            else:
                break
        
        if not num_s:
            return 0
        
        num = flag * int(num_s)
        
        bound = 2**31
        if num < -1* bound:
            return  -1* bound
        elif num > bound-1:
            return  bound-1
        else:
            return num
        
