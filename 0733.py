class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        M, N = len(image), len(image[0])
        
        same = image[sr][sc]
        if same == newColor: return image
        image[sr][sc] = newColor
        q = [[sr, sc]]
        while len(q) > 0:
            r, c = q.pop(0);
            for i, j in direction:
                x, y = r+i, c+j
                if (0 <= x < M and 0 <= y < N and image[x][y] == same):
                    image[x][y] = newColor
                    q.append([x, y])
        return image
        
