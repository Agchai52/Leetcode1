class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1 or num == 4:
            return True
        if num < 4:
            return False
        
        low, high = 0, num // 2
        
        while low <= high: # until empty set
            mid = (low + high) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
