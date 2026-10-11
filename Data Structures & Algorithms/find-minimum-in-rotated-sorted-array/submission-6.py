class Solution:
    def findMin(self, nums: List[int]) -> int:
            # two island
            # one side has the number
            # first nums[l] < nums[r]: return nums[l]
            # get mid point
            # cases
            # so if the mid point is smaller the left
            # if mid is bigger then left
            # if mid is smaller then right
            # if mid is bigger then right
            # so rule is use right ancor
            # if mid is bigger then right
            #     l = mid + 1
            # if mid is small then right
            #     r = mid - 1
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (right - left) // 2 + left

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]



