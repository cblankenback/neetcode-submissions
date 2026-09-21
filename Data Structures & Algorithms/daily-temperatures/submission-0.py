class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        seen = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while seen and seen[-1][0] < temp:
                prevTemp, prevIndex = seen.pop()
                res[prevIndex] = index - prevIndex
            seen.append([temp, index])
        return res
