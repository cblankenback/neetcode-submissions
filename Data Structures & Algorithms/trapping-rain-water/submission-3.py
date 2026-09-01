class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        maxL, maxR = height[0], height[len(height) - 1]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                res +=(max(min(maxL, maxR)- height[l], 0))
            else:
                r -=1
                maxR = max(maxR, height[r])
                res+=(max(min(maxL, maxR)- height[r],0))
       
        return res