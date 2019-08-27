class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # Method 1: BFS
        if len(rooms) == 0: return rooms
        m, n = len(rooms), len(rooms[0])
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] != 0:
                    continue
                q.append((i,j))
                
        while q:
            x, y = q.pop(0)
            #print('===')
            #print(x,y)
            val = rooms[x][y] + 1
            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                row = x + a
                col = y + b
                if 0 <= row < m and 0 <= col < n and rooms[row][col] == 2147483647:
                    
                    #print(row,col)
                    rooms[row][col] = min(rooms[row][col], val)
                    q.append((row, col))
        
