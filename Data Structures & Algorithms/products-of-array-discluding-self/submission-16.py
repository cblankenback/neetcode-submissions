class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        postfix = 1
        postarry = [1] * (len(nums))
        prefixarry = [1] * (len(nums))
        for i, n in enumerate(nums):
            prefixarry[i] = prefix
            prefix =  n * prefix
        
        for i in range(len(nums)-1, -1, -1):
            postarry[i] = postfix
            postfix = postarry[i] * nums[i]
        
        res = [1] *  (len(nums))
        for i in range(len(nums)-1, -1, -1):
            res[i] = prefixarry[i] * postarry[i]

        return res
        