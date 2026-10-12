class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (right - left) // 2 + left

            if nums[mid] < nums[right]:
                #search left side since we are already in the small side
                # but we could already be at smallest
                right = mid
            else:
                left = mid + 1
        return nums[left]