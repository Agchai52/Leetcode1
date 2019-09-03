import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        '''
        1. distance^2 = x^2 + y^2 for point(x,y)
        2. heap = [(distance, [x,y])]
        3. pop from heap k times
        '''
        if K == 0: return []
        if K == 1 and len(points) == 1: return points
        # Method 1: heap O(N) + O(Klog(N))
        '''
        heap = []
        res = []
        for (x, y) in points:
            dis2 = x ** 2 + y ** 2
            heap.append((dis2, [x, y]))
        heapq.heapify(heap)
        for _ in range(K):
            if not heap: return res
            _, point = heapq.heappop(heap)
            res.append(point)
        return res
        '''
        # Method 2: sort O(NlogN)
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
