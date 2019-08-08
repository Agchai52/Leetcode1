class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [i+1 for i in range(n)]
        self.dfs(nums, res, [], k)
        return res
    
    def dfs(self, nums, res, path, k):
        if k > len(nums):
            return 
        if k == 0:
            res.append(path)
        for i in xrange(len(nums)):
            self.dfs(nums[i+1:], res, path+[nums[i]], k-1)
            
