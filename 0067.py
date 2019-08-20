class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Method 1:
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
        
        # Method 2:
        res = ''
        i = len(a) - 1
        j = len(b) - 1
        flag = 0
        while i >= 0 or j >= 0:
            int_a = int(a[i]) if i >= 0 else 0
            int_b = int(b[j]) if j >= 0 else 0
            digit = int_a + int_b + flag     
            if digit > 1:
                digit -= 2
                flag = 1
            else:
                flag = 0
            res = str(digit) + res
            i -= 1
            j -= 1
        
        if flag == 1:
            res = '1' + res
        return res
    
        # Method 3:
        return bin(int(a,2)+int(b,2))[2:]
