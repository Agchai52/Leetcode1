"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
    # Method 1: DFS
    #    node_copy = self.dfs(node, dict())
    #    return node_copy
    #
    #def dfs(self, node, hashd):
    #    if not node: return None
    #    if node in hashd: return hashd[node]
    #    node_copy = Node(node.val, [])
    #    hashd[node] = node_copy
    #    for n in node.neighbors:
    #        n_copy = self.dfs(n, hashd)
    #        if n_copy:
    #            node_copy.neighbors.append(n_copy)
    #    return node_copy
            
    # Method 2: BFS
        que = []
        hashd = dict()
        que.append(node)
        node_copy = Node(node.val, [])
        hashd[node] = node_copy
        while que:
            t = que.pop(0)
            if not t: continue
            for n in t.neighbors:
                if n not in hashd:
                    hashd[n] = Node(n.val, [])
                    que.append(n)
                hashd[t].neighbors.append(hashd[n])
        return node_copy
