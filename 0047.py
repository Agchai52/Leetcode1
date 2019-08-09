class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Method 1: Backtrack
        if not nums: return [[]]
        if len(nums) == 1: return [nums]
        nums.sort()
        res = []
        visited = [0] * len(nums)
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            for i in xrange(len(nums)):
                if i > 0 and visited[i-1] == 0 and nums[i] == nums[i-1]:
                    continue 
                if visited[i] == 0:
                    visited[i] = 1
                    dfs(path+[nums[i]])
                    visited[i] = 0
        dfs([])
        return res
