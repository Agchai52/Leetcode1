class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        # Method 1: Recursion
        if n == 1: return 0
        if n % 2 == 0: 
            return 1 + self.integerReplacement(n/2)
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        '''
        
        # Method 2: except for 3, 0b...11 + 1 and 0b...01 - 1 faster
        count = 0
        while n > 1:
            count += 1
            if n % 2 == 0:
                n = n / 2  # or n >>= 1            
            else:
                if n & 2 and n != 3: # 0b...11 
                    n += 1
                else: # 0b...01 and 3
                    n -= 1
        return count
                
        
