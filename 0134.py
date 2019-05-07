class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        sums = 0
        start = 0
        
        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            sums = sums + gas[i] - cost[i]
            if sums < 0:
                start = i + 1
                sums = 0
        
        if total < 0:
            return -1
        else:
            return start
