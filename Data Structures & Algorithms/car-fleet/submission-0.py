class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, speed] for pos, speed in zip(position,speed)]
        stack = []
        for pos, speed in sorted(pair)[::-1]:
            # speed * time + pos = target
            # (target - pos)/ speed = time
            time = (target - pos) / speed
            stack.append(time)
            # 5
            # 3
            # 3<= 5
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            


