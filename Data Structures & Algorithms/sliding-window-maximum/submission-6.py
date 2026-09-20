class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        left = 0
        res = []
        for right in range(len(nums)):
            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()
            deque.append(right)
                                    # 0 < 1
            if deque[0] < left:
                deque.popleft()
            
            if right + 1 >= k:
                res.append(nums[deque[0]])
                left += 1
        return res
