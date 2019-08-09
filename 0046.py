class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # Method 1: Recursion
        
    #    res = []
    #    self.dfs(nums, [], res)
    #    return res
    #
    #def dfs(self, nums, path, res):
    #    if not nums:
    #        res.append(path)
    #    for i in xrange(len(nums)):
    #        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
    # Method 2: Backtrack
    #    if not nums: return [[]]
    #    if len(nums) == 1: return [nums]
    #    res = []
    #    visited = [0] * len(nums)
    #    
    #    def dfs(path):
    #        if len(path) == len(nums):
    #            res.append(path)
    #        for i in xrange(len(nums)):
    #            if visited[i] == 0:
    #                visited[i] = 1
    #                dfs(path+[nums[i]])
    #                visited[i] = 0
    #    dfs([])
    #    return res
            
    # Method 3: Python
        from itertools import permutations
        return list(permutations(nums))
