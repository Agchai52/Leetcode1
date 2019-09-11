class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B: return True
        if len(A) != len(B): return False
        
        def shift(C):
            A = C[1:] + C[0]
            return A
            
        
        n = len(A)
        while n > 0:
            A = shift(A)
            if A == B:
                return True
            n -= 1
        return False
            
            
        
        
