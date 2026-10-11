class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = (right - left) // 2 + left
            # mid is eating rate
            # so we should get the total time and see if rate needs to increase or decrease    
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            
            if time > h:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid - 1
        return res
