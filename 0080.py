class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        
        if len(nums) <= 2:
            return len(nums)
        pre = 0
        count = 1
        cur = 1
        while cur < len(nums):
            if nums[pre] == nums[cur] and count == 2:
                cur += 1
            else:
                if nums[pre] == nums[cur]:
                    count = count+1
                else:
                    count = 1
                pre = pre +1                
                nums[pre] = nums[cur]
                cur = cur +1
        return pre + 1 
        
