class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        lowest = prices[l]
        highest = 0
        res = 0
        while r < len(prices):
            if prices[r] < lowest:
                lowest = prices[r]
                highest = 0
                l = r
                if l + 1 < len(prices):
                    
                    r = l + 1
            highest = max(highest, prices[r])
            res = max(highest - lowest, res)

            r += 1
        return res
