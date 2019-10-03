class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # Method 1
        '''
        1. check if words1 == words2
        3. check if lens of lists are equal
        4. use a dict to save pairs
        5. traverse i in lists check : equal or find similar in dic        
        '''
        
        if words1 == words2: return True
        
        w1 = words1
        w2 = words2
        
        if len(w1) != len(w2): return False
        
        dmap = collections.defaultdict(list)
        for p in pairs:
            dmap[p[0]].append(p[1])
            dmap[p[1]].append(p[0])
            
        for i in range(len(w1)):
            if w1[i] != w2[i] and w2[i] not in dmap[w1[i]]:
                return False
        
        return True
