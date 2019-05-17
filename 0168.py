class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        sheet = ''
        while n != 0:
            sheet = uppers[(n-1)%26] + sheet
            n = (n-1)/26
        
            
            
        return sheet
