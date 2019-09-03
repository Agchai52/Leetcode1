class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        1. start <= end:
           -start = max(A[i][0],B[j][0])
           -end = min(A[i][1],B[j][1])
        2. i++: A[i][1]<B[j][0]
        3. j++: A[i][0]>B[j][0]
        '''
        
        if not A or not B: return []
        res = []
        i, j = 0, 0
        start, end = 0, 0
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif A[i][0] > B[j][1]:
                j += 1
            else:
                start = max(A[i][0],B[j][0])
                end = min(A[i][1],B[j][1])
                if start <= end:
                    res.append([start, end])
                if A[i][1] < B[j][1]:
                    i += 1
                elif A[i][1] > B[j][1]:
                    j += 1
                else:
                    i += 1
                    j += 1
        return res
