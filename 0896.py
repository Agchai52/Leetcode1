class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        '''
        1. convert to ascending order
      
        '''
        # Method 1:
        #if not A: return False
        #if len(A) == 1: return True
        #if A[0] > min(A):
        #    A = A[::-1]    
        #for i in range(1,len(A)):
        #    if A[i-1] > A[i]:
        #        return False
        #return True
    
        # Method 2:
        if not A: return False
        if len(A) == 1: return True
        store = 0
        for i in range(1,len(A)):
            c = cmp(A[i-1], A[i])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True
        
