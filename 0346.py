class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.maxLen = size
        self.q = []
        self.sum = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.sum += val
        l = len(self.q)
        if l <= self.maxLen:           
            return float(self.sum) / l
        else:
            pre = self.q.pop(0)
            self.sum -= pre
            return float(self.sum) / self.maxLen
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
