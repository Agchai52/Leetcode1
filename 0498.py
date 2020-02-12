class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        result = []
        direction = [(-1, 1), (1, -1)]
        count = 0
        i, j = 0, 0 # row, col
        while len(result) < m * n:
            if 0 <= i < m and 0 <= j < n:
                result.append(matrix[i][j])
                cur_dir = direction[count % 2]
                i, j = i + cur_dir[0], j + cur_dir[1]
                continue
            elif i < 0 and 0 <= j < n:
                i += 1
            elif 0 <= i < m and j < 0:
                j += 1
            elif i >= m and j < n:
                i -= 1
                j += 2
            elif i < m and j >= n:
                j -= 1
                i += 2
            count += 1
        return result
