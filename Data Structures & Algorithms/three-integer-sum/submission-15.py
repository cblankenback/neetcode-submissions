class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
# If the lowest number is > 0, the sum can never be 0
            if nums[i] > 0:
                break
                
            # Skip duplicate values for 'i'
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                triplets = nums[i] + nums[l] + nums[r]
                if triplets == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # Move BOTH pointers inward
                    l += 1
                    r -= 1
                    
                    # Skip duplicate values for 'l' so we don't record the exact same triplet
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif triplets > 0:
                    r -= 1
                else:
                    l += 1
        return res
            