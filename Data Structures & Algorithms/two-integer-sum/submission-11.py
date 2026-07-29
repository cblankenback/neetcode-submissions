class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # num -> idx
        # target = num + x
        # target - num = x
        for i, num in enumerate(nums):
            if hashmap.get(target - num) != None:
                return [hashmap[target - num], i]
            hashmap[num] = i
