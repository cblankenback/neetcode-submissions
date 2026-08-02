class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # key number 
        # value count
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        # key count
        # value number

        for n, c in counts.items():
            buckets[c].append(n)
        

        res = []

        for i in range(len(buckets)-1, 0, -1):
            bucket = buckets[i] 
            for number in bucket:
                if len(res) == k:
                    return res
                res.append(number)
        return res

