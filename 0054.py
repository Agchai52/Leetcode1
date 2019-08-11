class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        res = []
        direct = 0 # right:0, down:1, left:2, up:3
        up = left = 0
        down, right = len(matrix)-1, len(matrix[0])-1
        while up <= down and left <= right:
            if direct == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            elif direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif direct == 2:
                for i in range(left, right+1)[::-1]:
                    res.append(matrix[down][i])
                down -= 1
            else:
                for i in range(up, down+1)[::-1]:
                    res.append(matrix[i][left])
                left += 1
            direct = (direct+1) % 4
        return res
