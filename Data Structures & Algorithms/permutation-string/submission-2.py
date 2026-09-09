class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        for s in s1:
            s1map[s] = s1map.get(s,0) + 1
        
        l = 0
        s2map = {}
        for r in range(len(s2)):
            s2map[s2[r]] = s2map.get(s2[r], 0) + 1
            
            if (r - l + 1) > len(s1):
                s2map[s2[l]] -= 1
                if s2map[s2[l]] == 0:
                    del s2map[s2[l]]  # Clean up so dict comparison works
                l += 1
            if s1map == s2map:
                return True
        return False
            
