class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        '''
        row 1: 0
        row 2: 01
        row 3: 0110
        row 4: 01101001
        '''
        if N == 1: return 0
        num = self.kthGrammar(N-1, (K+1)/2)
        if num == 0:
            if K % 2 == 0: return 1
            else: return 0
        else:
            if K % 2 == 0: return 0
            else: return 1
