class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        res = 0 
        for r in range(len(s)):
            #(r - l + 1) - most common <= k
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            while r > 0 and (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] = hashmap.get(s[l], 0) - 1
                l += 1
            

            res = max(res, r - l + 1)
        return res
            