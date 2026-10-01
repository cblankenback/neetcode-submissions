class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        pointer = (len(nums) -1) // 2 
        l = 0
        r = len(nums) -1 
        while l <= r:
            if nums[pointer] == target:
                return pointer
            elif nums[pointer] > target:
                r = pointer - 1
                pointer = l + (r - l) // 2
            else:
                l = pointer + 1
                pointer = l + (r - l) // 2
        return -1
