class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # https://blog.csdn.net/fuxuemingzhu/article/details/83027364
        # Method 1: LIS dp 
        if not nums: return []
        n = len(nums)
        dp, parent = [0] * n, [0] * n
        mx, mx_ind = 0, -1
        nums.sort()
        res = []
        for i in range(n):
            for j in range(i): #(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_ind = i
        for k in range(mx + 1):
            res.append(nums[mx_ind])
            mx_ind = parent[mx_ind]
        return res[::-1]
                        
        
