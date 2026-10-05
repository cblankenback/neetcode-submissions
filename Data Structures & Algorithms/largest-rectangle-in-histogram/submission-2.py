class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                lastIndex, lastHeight = stack.pop()
                area = lastHeight * (index - lastIndex)
                start = lastIndex
                res = max(res, area)

            stack.append([start, height])
        
        for index, height in stack:
            
            area = (len(heights) - index) * height
            res = max(area, res)
        return res