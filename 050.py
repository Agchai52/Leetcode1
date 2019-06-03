class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.
        
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1.
        
        while n:
            if n % 2:
                ans *= x
            n >>= 1 # n = n // 2 ** 1    
            x *= x            
        return ans
