class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]
        for i in xrange(3, n):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        return max(dp[-1], dp[-2])
