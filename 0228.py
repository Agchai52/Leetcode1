class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        if len(nums) == 1: return [str(nums[0])]
        res = []
        pre = nums[0]
        path = [str(pre)]
        for i in xrange(1, len(nums)):
            cur = nums[i]
            if cur > pre + 1:
                res.append('->'.join(path))                
                path = [str(cur)]
                pre = cur
                if i == len(nums)-1:
                    res.append('->'.join(path))                
                continue
            if len(path) < 2:
                path.append(str(cur))
            else:
                path[-1] = str(cur)
            if i == len(nums)-1:
                res.append('->'.join(path))                
                path = []
            pre = cur
        return res
