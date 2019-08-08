class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    # Method 1: DFS
    #    res = []
    #    candidates.sort()
    #    self.dfs(candidates, 0, res, [], target)
    #    return res
    #
    #def dfs(self, array, index, res, path, target):
    #    if target < 0:
    #        return
    #    if target == 0:
    #        res.append(path)
    #        return
    #    for i in xrange(index, len(array)):
    #        self.dfs(array, i, res, path+[array[i]], target-array[i])
    
    
