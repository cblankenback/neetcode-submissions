class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            arr = [0] * 26 
            for l in str:
                arr[ord(l) - ord('a')] += 1
            res[tuple(arr)].append(str)
        return list(res.values())