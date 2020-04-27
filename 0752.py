class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def get_neighbor(node):
            for i in xrange(4):
                c = int(node[i])
                for d in (-1, 1):
                    y = (c + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        
        dead = set(deadends)
        q = collections.deque([('0000', 0)])
        seen = set()
        seen.add('0000')
        while q:
            node, depth = q.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in get_neighbor(node):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))
        return -1
            
