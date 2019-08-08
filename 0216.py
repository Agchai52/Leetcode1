class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        array = [i+1 for i in xrange(9)]
        self.dfs(array, k, res, [], n)
        return res
    
    def dfs(self, array, k, res, path, target):
        if target < 0:
            return
        if k > len(array):
            return
        if k == 0 and target == 0:
            res.append(path)
        for i in xrange(len(array)):
            self.dfs(array[i+1:], k-1, res, path+[array[i]], target-array[i])
