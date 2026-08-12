class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # One-liner to convert the list to a hash set
        numset = set(nums)
        highestcount = 0

        for num in numset:
            # ONLY start counting if this number is the start of a sequence
            if (num - 1) not in numset:
                count = 1
                check = num
                
                # Count upwards as long as the next number exists
                while (check + 1) in numset:
                    check += 1
                    count += 1
                
                # Update our highest count
                if count > highestcount:
                    highestcount = count
                    
        return highestcount