import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        table = {}
        freq = []
        res = []
        for w in words:
            if w not in table:
                table[w] = 1
            else:
                table[w] += 1
        for w, f in table.items():
            freq.append((-f, w))
        heapq.heapify(freq)
        for _ in range(k):
            res.append(heapq.heappop(freq)[1])
        return res
