import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = []
        for i, val in enumerate(self.nums):
            if val == target:
                index.append(i)
        #return index[random.randint(0, len(index)-1)]
        return index[random.randrange(0, len(index))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
