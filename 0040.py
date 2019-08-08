class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, 0, res, [], target)
        return res
    
    def dfs(self, array, index, res, path, target):
        if target < 0:
            return
        if target == 0 and path not in res:
            res.append(path)
            return
        for i in xrange(index, len(array)):
            if i > index and array[i] == array[i-1]:
                continue
            self.dfs(array, i+1, res, path+[array[i]], target-array[i])
