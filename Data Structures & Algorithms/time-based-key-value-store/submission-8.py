class TimeMap:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        to_search = self.data.get(key, [])
        left = 0
        right = len(to_search) - 1
        res = ""
        while left <= right:
            mid = (right - left) // 2 + left

            if to_search[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                res = to_search[mid][0]
        return res 



