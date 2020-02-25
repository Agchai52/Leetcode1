class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        elif rowIndex == 1: return [1,1]
        
        prev_row = [1,1]
        
        for r in range(2, rowIndex + 1):
            cur_row = [1] * (r + 1)
            for c in range(1, r):
                cur_row[c] = prev_row[c-1] + prev_row[c]
            prev_row = cur_row
        return cur_row
