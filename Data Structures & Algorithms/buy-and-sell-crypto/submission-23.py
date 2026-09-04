class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        lowest = prices[l]
        
        res  = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(prices[r] - prices[l], res)
            else:
                prices[l] = prices[r]
                l = r
                
            r+=1
        return res
            