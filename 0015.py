class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Method 1: TLE
        # nums.sort()
        # res = []
        # for i in xrange(len(nums)-1):
        #     if i >0 and nums[i] == nums[i-1]:
        #         continue
        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         t = nums[i] + nums[l] + nums[r]
        #         if t == 0:
        #             if [nums[i], nums[l], nums[r]] not in res:
        #                 res.append([nums[i], nums[l], nums[r]])
        #             l = l + 1
        #             r = r - 1
        #         elif t < 0:
        #             l = l + 1
        #         else:
        #             r = r - 1
        # return res
                                
        # Method 2: AP    
        N = len(nums)
        nums.sort()
        res = []
        for t in range(N - 2):
            if t > 0 and nums[t] == nums[t - 1]:
                    continue
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if _sum == 0:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif _sum < 0:
                    i += 1
                else:
                    j -= 1
        return res
