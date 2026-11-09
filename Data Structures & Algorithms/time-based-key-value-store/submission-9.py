class TimeMap:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        to_check = self.data.get(key, [])
        left = 0
        right = len(to_check) - 1
        res = ""
        while left <= right:
            mid = (right - left) // 2 + left

            if to_check[mid][1] <= timestamp:
                left = mid + 1
                res = to_check[mid][0]
            else:
                right = mid - 1
        return res
        
