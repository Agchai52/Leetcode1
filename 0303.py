class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #self.array = nums
        self.array = [0] * (len(nums)+1)
        for i in xrange(len(nums)):
            self.array[i+1] = self.array[i] + nums[i]
            

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #return sum(self.array[i:j+1])
        return self.array[j+1] - self.array[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
