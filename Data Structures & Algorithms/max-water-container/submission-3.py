class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = height * width
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] == heights[r]:
                if heights[l + 1] > heights[r -1]:
                    r -=1
                else:
                    l += 1
        return res
