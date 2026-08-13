class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        highest = 0
        for num in nums:
            count = 0
            if num - 1 not in numset:
                x = num
                while x in numset:
                    x = x + 1
                    count += 1
            if count > highest:
                highest = count
        return highest