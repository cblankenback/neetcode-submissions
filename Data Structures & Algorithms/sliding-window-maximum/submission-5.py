class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque 
        # add index (nums[index]) so we dont need number stored
        # if right most element is less then current then remove
        # keep doing that un pos
        # then if window is at size k then also remove left most element 
        # then res add left most element 
        # increase left

        deque = collections.deque()

        left = 0
        res = []
        for right in range(len(nums)):
            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()
            deque.append(right)

            if deque[0] < left:
                deque.popleft()

            if right >= k-1:
                res.append(nums[deque[0]])
                left += 1
        return res






            
