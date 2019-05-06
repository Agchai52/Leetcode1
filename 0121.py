class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_p = prices[0]
        max_p = 0
        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i] - min_p > max_p:
                max_p = prices[i] - min_p            
                
        return max_p
