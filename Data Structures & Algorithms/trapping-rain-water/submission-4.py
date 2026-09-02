class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxl = height[l]
        maxr = height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxl = max(maxl, height[l])
                res += max(min(maxl,maxr) - height[l], 0)
            else:
                r-= 1
                maxr = max(maxr, height[r])
                res += max(min(maxl,maxr) - height[r], 0)
        return res