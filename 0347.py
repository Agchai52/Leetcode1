class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ## Method 1: Bucket Sort
        #dic, res = {}, []
        #bucket = [[] for _ in xrange(len(nums) + 1)]
        #for num in nums:
        #    dic[num] = dic[num] + 1 if num in dic else 1
        #for key in dic:
        #    bucket[dic[key]].append(key)
        #for i in xrange(len(bucket)-1, 0-1, -1):
        #    if bucket[i]:
        #        res.extend(bucket[i])
        #    if len(res) >= k:
        #        break
        #return res[:k]
            
        # Method 2: Priority Queue
        #dic, res, pq = {}, [], []
        #for num in nums:
        #    dic[num] = dic[num] + 1 if num in dic else 1
        #for key in dic:
        #    heapq.heappush(pq, (-dic[key], key))
        #for i in xrange(k):
        #    res.append(heapq.heappop(pq)[1])
        #return res
    
        # Method 3: Python collection
        counter = collections.Counter(nums)
        return [item[0] for item in counter.most_common(k)]
