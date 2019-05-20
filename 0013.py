class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Method 1 (self)
        # s = list(s)
        # roman = list('MDCLXVI')
        # integer = [1000, 500, 100, 50, 10, 5, 1]
        # num = 0
        # 
        # indices = map(roman.index, s)
        # i = 0
        # while i < len(indices):
        #     digit = integer[indices[i]]
        #     if i < len(indices)-1 and indices[i+1] < indices[i]:
        #         digit_aft = integer[indices[i+1]]
        #         digit = digit_aft - digit
        #         i += 1
        #     num = num + digit
        #     i += 1
        # return num
        
        # Method 2
        digits = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        min_d = 1
        for i in xrange(len(s)-1, -1, -1):
            if digits[s[i]] >= min_d: 
                min_d = digits[s[i]]
                num = num + digits[s[i]]
            else:                
                num = num - digits[s[i]]
        return num
