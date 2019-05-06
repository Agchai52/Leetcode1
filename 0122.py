class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_p = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                max_p = max_p + (prices[i+1] - prices[i])
        return max_p
