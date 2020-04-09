class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ''' Method 2: equation
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
        '''
        G = [0] * (n+1)
        G[0], G[1] = 1, 1
        
        for k in range(2, n+1):
            for i in range(1, n+1):
                G[k] += G[i-1] * G[k-i]
        return G[n]
