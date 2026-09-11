class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        seen = {}
        s1seen = {}
        totalmatch = 0
        for s in s1:
            s1seen[s] = s1seen.get(s, 0) + 1
            
        matches = 0
        totalmatch = len(s1seen)
        for r in range(len(s2)):
            
            seen[s2[r]] = seen.get(s2[r], 0) + 1
            if seen.get(s2[r], 0) == s1seen.get(s2[r], -1):
                matches += 1
            

            if (r - l + 1) == len(s1) and matches == totalmatch:
                return True
            elif (r - l + 1) == len(s1) and matches != totalmatch:
                if seen[s2[l]] == s1seen.get(s2[l], 0):
                    matches -= 1
                seen[s2[l]] -= 1

                if seen[s2[l]] == 0:
                    seen.pop(s2[l])
                l += 1

            
        return False