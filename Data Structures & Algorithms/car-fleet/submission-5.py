class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, speed] for pos, speed in zip(position, speed)]

        pair = sorted(pair, reverse=True)
        stack = []
        
        for pos, speed in pair:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= time:
                stack.pop()
        return len(stack)
            

