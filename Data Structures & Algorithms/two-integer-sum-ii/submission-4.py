class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            current_sum = numbers[l] + numbers[r]
            
            if current_sum == target:
                # The problem asks for 1-indexed array, so we add 1
                return [l + 1, r + 1]
                
            elif current_sum > target:
                # The sum is too big! 
                # Since the array is sorted, how do we make the sum smaller?
                r -= 1
                
            else:
                # The sum is too small!
                # How do we make the sum bigger?
                l += 1