class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Method: Topological Sort BFS
        if len(words) == 0: return ''
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        res =''
        # create empty hash table for each letter
        for word in words:
            for c in word:
                if c not in indegree:
                    indegree[c] = 0
        # Construct the graph & indegree
        for i in xrange(1, len(words)):
            k, len1, len2 = 0, len(words[i-1]), len(words[i])
            while k < min(len1, len2) and words[i-1][k] == words[i][k]:
                k += 1
            if k >= min(len1, len2):
                continue
            indegree[words[i][k]] += 1
            graph[words[i-1][k]].append(words[i][k])
        
        # Find zero indegree letter and put into res, then all its children indegree--
        
        for _ in indegree:
            zeroDegree = False
            for val in indegree:
                if indegree[val] == 0:
                    zeroDegree = True
                    break
            if zeroDegree == False: return ''
            res += val
            indegree[val] -= 1
            for c in graph[val]:
                indegree[c] -= 1
        return res
            
                
