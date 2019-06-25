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
        
        N = len(nums) 
        
        return max(self.rob_range(nums[0:N-1]), self.rob_range(nums[1:N]))
        
        
        
    def rob_range(self, nums):
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        N = len(nums) 
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in xrange(2, N):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
