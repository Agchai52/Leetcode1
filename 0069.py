class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        low, high = 1, x/2
        
        last = 0
        
        while low <= high:
            mid = (low + high) / 2
            if mid * mid < x:
                low = mid + 1 
                last = mid
            elif mid * mid > x:
                high = mid - 1
            else:
                return mid
        return last
