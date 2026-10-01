class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        start = 0
        maxArea = 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] >= height:
                lastInx, lastHght = stack.pop()
                area = lastHght * (index - lastInx)
                start = lastInx
                maxArea = max(maxArea, area)


            stack.append([start, height])

        for index, height in stack:
            area = (len(heights) - index) * height
            maxArea = max(maxArea, area)
        return maxArea