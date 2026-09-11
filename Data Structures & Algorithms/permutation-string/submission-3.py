class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        seen = {}
        s1seen = {}
        for s in s1:
            s1seen[s] = s1seen.get(s, 0) + 1
        for r in range(len(s2)):
            seen[s2[r]] = seen.get(s2[r], 0) + 1
            print(s1seen)
            print(seen)
            if (r - l + 1) == len(s1) and s1seen == seen:
                return True
            elif (r - l + 1) == len(s1) and s1seen != seen:
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    seen.pop(s2[l])
                l += 1

            
        return False