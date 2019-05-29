class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Method 1 # doesn't mean it, have to do digit by digit 
        #n1, n2 = 0, 0
        #for i in xrange(len(num1)):
        #    n1 = n1*10 + int(num1[i])
        #for j in xrange(len(num2)):
        #    n2 = n2*10 + int(num2[j]) 
        #return str(n1 * n2)
        
        # Method 2 
        if num1 == '0' or num2 == '0':
            return '0'
        ans = 0
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            cur = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1)-ord('0')) * (ord(n2)-ord('0'))
                first, second = multi // 10, multi % 10
                cur += (second + pre) * (10 ** j)
                pre = first
            cur += pre * (10 ** len(num1))
            ans += cur * (10 ** i)
        return str(ans)
        
