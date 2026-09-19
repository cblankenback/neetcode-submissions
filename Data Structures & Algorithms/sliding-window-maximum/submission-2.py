class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []

        left = 0
        for right in range(len(nums)):
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()

            deque.append(right)

            if deque[0] < left:
                deque.popleft()
            
            if  right - left + 1 == k:
                res.append(nums[deque[0]])
                left += 1
        return res