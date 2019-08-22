class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]] m x n
        :type B: List[List[int]] n x p
        :rtype: List[List[int]] m x p
        """
        # Method 1
        m, n, p = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in xrange(p)] for _ in xrange(m)]
        for i in xrange(m):
            for k in xrange(n):
                if A[i][k] != 0:
                    for j in xrange(p):
                        C[i][j] += A[i][k] * B[k][j]
        return C
        
        # Method 2:
        '''
        def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    m, p = len(A), len(B[0])
    Ai = [[i for i, v in enumerate(r) if v] if any(r) else [] for r in A]
    res = [[0] * p for i in range(m)]
    for i, r in enumerate(Ai):
        if not r:
            continue
        for k in range(p):
            for j, v in enumerate(r):
                res[i][k] += A[i][v] * B[v][k]
    return res

        '''
