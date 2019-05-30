class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # log(n) TLE, so binary: add and minus
        if abs(dividend) < abs(divisor):
            return 0
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        a = abs(dividend)
        b = abs(divisor)
        
        res = 0
        
        sums, count = 0, 0
        while a >= b:
            sums = b
            count = 1
            while sums + sums <= a:
                sums += sums
                count += count
            a -= sums
            res += count
        
        
        
        res = res * sign
        bound = 2**31
        if res < -bound:
            return -bound
        elif res > bound -1:
            return bound-1
        else:
            return res
