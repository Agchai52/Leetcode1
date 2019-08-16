class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        l, r = 0, 0
        res = float('inf')
        sums = 0
        while r < len(nums):
            sums += nums[r]
            while sums >= s:
                res =a min(res, r - l + 1)
                sums -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0
