class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res
    
    def dfs(self, nums, index, res, path):
        
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, res, path + [nums[i]])
