# Binary
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n, left, right = len(citations), 0, len(citations)-1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] >= n - mid:
                right = mid - 1
                
            else:
                left = mid + 1
        return n - left
