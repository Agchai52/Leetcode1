class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = 0, 0
        for i in xrange(len(num1)):
            n1 = n1*10 + int(num1[i])
        for j in xrange(len(num2)):
            n2 = n2*10 + int(num2[j])
        
        return str(n1 * n2)
