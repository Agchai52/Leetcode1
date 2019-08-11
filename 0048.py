class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            m = len(matrix)
            # up side down
            for i in xrange(m/2):
                for j in xrange(m):
                    matrix[i][j], matrix[m-i-1][j] = matrix[m-i-1][j], matrix[i][j]
            # mirror
            for i in xrange(m):
                for j in xrange(i):
                    if i == j or i < j:
                        continue
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
                
                    
