class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
    # Method 1: DFS
        table = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1.0 / value
        return [self.dfs(table, x, y, set()) if x in table and y in table else -1.0 for (x,y) in queries]
    
    def dfs(self, table, x, y, visited):
        if x == y: return 1.0
        visited.add(x)
        for n in table[x]:
            if n in visited: continue
            visited.add(n)
            d = self.dfs(table, n, y, visited)
            if d > 0:
                return d * table[x][n]
        return -1.0
