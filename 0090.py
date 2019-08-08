class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # Method 1
    #    res = []
    #    nums.sort()
    #    self.dfs(nums, 0, res, [])    
    #    return res
    #
    #
    #def dfs(self, nums, index, res, path):
    #    if path not in res:
    #        res.append(path)
    #    for i in xrange(index, len(nums)):
    #        if i > index and nums[i] == nums[i-1]:
    #            continue
    #        self.dfs(nums, i+1, res, path + [nums[i]])
    
    # Method 2:
        def dfs(depth, index, path):
            if path not in res: res.append(path)
            if depth == len(nums): return
            for i in xrange(index, len(nums)):
                dfs(depth+1, i+1, path+[nums[i]])
            
        nums.sort()
        res = []
        dfs(0, 0, [])
        return res
        
