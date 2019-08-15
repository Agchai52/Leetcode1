class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Method 1: DP Time = O(n), Space = O(1)
        hold = -float('inf')
        sold, rest = 0, 0
        for price in prices:
            pre_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, pre_sold)
        return max(rest, sold)
