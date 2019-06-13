class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Method 1: #15 3Sum+
        #nums.sort()
        #res = []
        #for i in xrange(len(nums)-2):
        #    for j in xrange(i+1, len(nums)-1):
        #        l, r = j+1, len(nums)-1
        #        while l < r:
        #            t = nums[i] + nums[j] + nums[l] + nums[r]
        #            if t == target:
        #                if [nums[i], nums[j], nums[l], nums[r]] not in res:
        #                    res.append([nums[i], nums[j], nums[l], nums[r]])
        #                l += 1
        #                r -= 1
        #            elif t < target:
        #                l += 1
        #            else:
        #                r -= 1
        #return res
                    
        # Method 2: Hash
        nums.sort()
        res, dic = set(), {}
        for p in xrange(len(nums)):
            for q in xrange(p+1, len(nums)):
                key = nums[p] + nums[q]
                if key not in dic:
                    dic[key] = [(p,q)]
                else:
                    dic[key].append((p,q))
                    
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)-2):
                T = target - nums[i] - nums[j]
                if T in dic:
                    for v in dic[T]:
                        if v[0] > j: res.add((nums[i],nums[j],nums[v[0]],nums[v[1]]))
        return [list(i) for i in res]
                    
                
            
