class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if not words: return False
        if len(words) == 1: return True
        table = {x:i for (i,x) in enumerate(order)}
        for i in xrange(1, len(words)):
            pre = words[i-1]
            cur = words[i]
            if not self.isSort(table, pre, cur):
                return False
        return True
    
    def isSort(self, table, pre, cur):
        l = min(len(pre), len(cur))
        i = 0
        while i < l:
            if table[pre[i]] < table[cur[i]]:
                return True
            elif table[pre[i]] > table[cur[i]]:
                return False
            i += 1
        if len(pre) > l:
            return False
        return True
