class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = set(nums)
        if len(a) == len(nums):
            return False
        else:
            return True
