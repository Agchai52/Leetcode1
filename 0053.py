class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        cur, pre = 0, 0
        res = float('-inf')
        for i in nums:
            cur = i + max(pre, 0)
            pre = cur
            res = max(res, cur)
        return res
