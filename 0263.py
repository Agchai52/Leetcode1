class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''
        1. num, mod = num / 2 or / 3 or / 5, %2 or %3 or %5
        2. while num != 1, if mod == 1
        3. num <= 0 return False
        '''
        if num <= 0: return False
        if num == 1: return True
        
        while num % 5 == 0:
            num = num / 5
        while num % 3 == 0:
            num = num / 3
        while num % 2 == 0:
            num = num / 2
       
        return True if num == 1 else False
