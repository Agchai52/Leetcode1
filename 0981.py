class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = collections.defaultdict(list)
        self.valueMap = collections.defaultdict(list)
        # self.maxTime = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timeMap[key].append(timestamp)
        self.valueMap[key].append(value)
        #self.maxTime[key] = max(self.maxTime[key], timestamp)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.timeMap:
            return ''
        
        def binarySearch(arr, key):
            l = 0
            r = len(arr)-1
            while l < r:
                m = (l + r) / 2
                if arr[m] == key:
                    return m
                    break
                elif arr[m] < key:
                    l = m + 1
                elif arr[m] > key:
                    r = m - 1
            return l
        if timestamp >= self.timeMap[key][-1]:
            return self.valueMap[key][-1]
        if timestamp == self.timeMap[key][0]:
            return self.valueMap[key][0]
        
        t = binarySearch(self.timeMap[key], timestamp)
        if t:
            return self.valueMap[key][t-1]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
