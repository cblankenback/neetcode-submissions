class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            maxProfit = max(prices[r] - prices[l], maxProfit)
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        return maxProfit

