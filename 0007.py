class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """        
    
        reverse = int(str(x)[::-1]) if x >=0 else -int(str(-x)[::-1])
        
        return reverse if reverse >= -2**31 and reverse <= 2**31 -1 else 0
