class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        for i in xrange(len(digits)-1, -1, -1):
            if digits[i] > 8:                
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)
        return digits
