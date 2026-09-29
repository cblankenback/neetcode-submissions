class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []

        for pos, speed in zip(position, speed):
            pair.append([pos,speed])
        pair = sorted(pair)[::-1]
        stack = []
        for pos, speed in pair:
            # dist = speed * time + pos
            # time =
            
            time = (target - pos) / speed
             
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
            
