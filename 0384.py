import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        
        # Method 1: Library
        # nums_s = self.nums[:]
        # random.shuffle(nums_s)
        # return nums_s
        
        #  Method 2: Fisher-Yates
        nums_s = self.nums[:]
        N = len(nums_s)
        for i in xrange(N):
            rand = random.randrange(i, N)
            nums_s[i], nums_s[rand] = nums_s[rand], nums_s[i]
        return nums_s
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
