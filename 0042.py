class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # https://blog.csdn.net/XX_123_1_RJ/article/details/81048041
        # Method 1: 
        #if not height: return 0
        #n = len(height)
        #res = 0
        #left_max = [0] * n
        #right_max = [0] * n
        #
        #left_max[0] = height[0]
        #right_max[n-1] = height[n-1]
        #
        #for i in range(1, n-1):
        #    left_max[i] = max(height[i], left_max[i-1])
        #
        #for i in range(n-2, -1, -1):
        #    right_max[i] = max(height[i], right_max[i+1])
        #    
        #for i in range(1,n-1):
        #    res += min(left_max[i], right_max[i]) - height[i]
        #return res
        
        # Method 2: two pointers
        if not height: return 0
        n, res = len(height), 0
        left_max, right_max = 0, 0
        left, right = 0, n-1
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            
            else:
                if height[right] < right_max:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res
        
