class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        '''
        num1 = '123', num2 = '1945'
        '''
        if not num1: return num1
        if not num2: return num2
        flag = 0
        res = ''
        l = min(len(num1),len(num2))
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        for i in range(l):
            total = int(num1[len(num1)-i-1]) + int(num2[len(num2)-i-1]) + flag
            if total >= 10:
                flag = 1
                total -= 10
            else:
                flag = 0
            res = str(total) + res
        
        if l < len(num1):
            for i in range(0,len(num1)-l)[::-1]:
                total = int(num1[i]) + flag
                if total >= 10:
                    flag = 1
                    total -= 10
                else:
                    flag = 0
                res = str(total) + res
        
        if flag > 0:
            res = '1' + res
        return res
