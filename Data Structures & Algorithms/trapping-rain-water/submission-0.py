class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0] * len(height)
        maxright = [0] * len(height) 
        maxl = 0
        maxr = 0
        res = 0
        for i in range(len(height)):
            maxleft[i] = max(maxl, height[i])
            maxl = max(maxl, height[i])
        for i in range(len(height)-1, -1, -1):
            maxright[i] = max(maxr, height[i])
            maxr = max(maxr, height[i])
        for i in range(len(height)):
            res += max(min(maxleft[i], maxright[i]) - height[i], 0)
        return res
