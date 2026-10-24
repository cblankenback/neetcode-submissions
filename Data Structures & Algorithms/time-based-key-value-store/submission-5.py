class TimeMap:

    def __init__(self):
        self.hashMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        row = self.hashMap.get(key, [])
        left = 0
        right = len(row) - 1
        res = ""
        while left <= right:
            mid = (right - left) // 2 + left

    
                
            if row[mid][1] > timestamp:
                right = mid - 1
            else:
                res = row[mid][0]
                left = mid + 1
        return res


        
