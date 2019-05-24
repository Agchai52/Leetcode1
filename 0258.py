class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        digits = [int(c) for c in s]
        sums = sum(digits)
        while sums >= 10:
            s = str(sums)
            digits = [int(c) for c in s]
            sums = sum(digits)
        
        return sums
