class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        most = 0
        while l < r:
            height = min(heights[l], heights[r])
            vol = height * (r - l)
            
            most = max(most, vol)
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                if heights[l+1] > heights[r-1]:
                    r -= 1
                else:
                    l+=1
        return most
