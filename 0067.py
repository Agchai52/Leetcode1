class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) >= len(b):
            s_max = a
            s_min = b
        else:
            s_max = b
            s_min = a
       
        if len(a) != len(b):
            diff = [0] * (len(s_max)-len(s_min))
            s_min = ''.join(str(e) for e in diff) + s_min
        ssum = ''
        flag = 0

        for i in xrange(len(s_max)-1, -1, -1):
            digit = int(s_max[i]) + int(s_min[i]) + flag
            flag = 0
            if digit >=  2:
                digit = digit - 2
                flag = 1
            ssum = str(digit) + ssum
        
        if flag > 0:
            ssum = str(flag) + ssum
        return ssum
