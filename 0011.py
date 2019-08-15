class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        # Method: two pointers, Time = O(n), Space = O(1)
        left, right = 0, len(h)-1
        res = 0
        while left < right:
            res = max(res, min(h[left], h[right])*(right - left))
            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
        return res
        
