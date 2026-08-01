class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # key: number 
        # value: count
        for n in nums:
            count[n] = count.get(n,0) + 1
        
        buckets = [[] for _ in range(len(nums)+ 1) ]

        for key, value in count.items():
            buckets[value].append(key)
        res = []
        j = 0
        for i in range(len(buckets)-1, 0, -1):

            for item in buckets[i]:
                if j == k:
                    return res
                res.append(item)
                j+= 1
    


        return res


            
