class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        prefixarr = [1] * len(nums)
        postfixarr = [1] * len(nums)
        for i in range(len(nums)):
            prefixarr[i] = prefix
            prefix = nums[i] * prefix
        for i in range(len(nums) -1 , -1 , -1):
            prefixarr[i] = prefixarr[i] * postfix
            postfix = nums[i] * postfix
       
        return prefixarr

