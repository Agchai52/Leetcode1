class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        row2cols = collections.defaultdict(list)
        for x, y in points:
            row2cols[x].append(y)
        
        lastx = {}
        ans = float('inf')
        
        for x in sorted(row2cols):
            cols_x = row2cols[x]
            cols_x.sort()
            for i, y2 in enumerate(cols_x):
                for j in xrange(i):
                    y1 = cols_x[j]
                    if (y1, y2) in lastx:
                        ans = min(ans, (y2 - y1)*(x - lastx[y1, y2]))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
