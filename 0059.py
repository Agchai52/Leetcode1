class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return [[1]]
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        direct = 0 # same as #54
        up, left = 0, 0
        down, right = n-1, n-1
        count = 0
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            elif direct == 1:
                for i in range(up, down+1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            elif direct == 2:
                for i in range(left, right+1)[::-1]:
                    count += 1
                    matrix[down][i] = count
                down -= 1
            else:
                for i in range(up, down+1)[::-1]:
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n*n:
                return matrix
            direct = (direct+1) % 4
            
        
