class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] >= height:
                i, h = stack.pop()
                start = i
                area = h * (index - i)
                res = max(area, res)
            stack.append([start,height])

        # what todo with remaining
        n = len(heights)
        for i, h in stack:
            area = h * (n - i)
            res = max(area, res)

        return res
            
