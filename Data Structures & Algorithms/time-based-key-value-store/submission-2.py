class TimeMap:

    def __init__(self):
        self.hashMap = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        self.hashMap[key]
        left = 0
        right = len(self.hashMap[key]) - 1
        res = ""
        while left <= right:
            
            mid = (right - left) // 2 + left
            values = self.hashMap.get(key, [])
            if values[mid][1] <= timestamp:
                res= values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
