class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key: array of char count, value: word
        res = {}
        for str in strs:
            arr = [0] * 26
            for l in str:
                arr[ord(l)- ord("a")] += 1
            key = tuple(arr)
            if key not in res:
                 res[key] = []

            res[tuple(arr)].append(str)
        return list(res.values())