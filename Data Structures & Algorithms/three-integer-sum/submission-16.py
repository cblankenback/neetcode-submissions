class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i-1] == nums[i]:
                    continue
            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                if triplet == 0 :
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif triplet > 0:
                    r -=1
                else:
                    l += 1
        return res