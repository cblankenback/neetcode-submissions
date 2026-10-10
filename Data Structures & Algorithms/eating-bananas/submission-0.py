class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            # mid is the eating speed
            mid = (r - l) // 2 + l
            # so now we need to see if this speed is less the h(time given)
            timeTaken = 0
            for pile in piles:
                timeTaken = timeTaken + math.ceil(pile/mid)
            # if it take longer then given time then we need to increase the eating speed so shift left
            if timeTaken > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res
        

