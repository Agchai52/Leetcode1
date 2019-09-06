class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        if n == 0: return False
        nums = set()
        while n not in nums:
            nums.add(n)
            total = 0
            s = str(n)
            for c in s:
                total += int(c) ** 2
            if total == 1:
                return True
            else:               
                n = total
        return False
