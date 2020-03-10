class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = set([n])
        while True:
            total = 0
            while n > 0:
                mod = n % 10
                total += mod ** 2
                n = (n - mod) / 10
            if total == 1:
                return True
            elif total in temp:
                return False
            else:
                temp.add(total)
                n = total
            
