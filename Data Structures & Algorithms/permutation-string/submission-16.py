class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for i in range(len(s1)):
            need[s1[i]] = need.get(s1[i], 0) + 1
        have = {}
        left = 0
        matching = len(need)
        currMatching = 0
        for right in range(len(s2)):
            
            #if by adding r does the matching go up or down
            if s2[right] in need:
                have[s2[right]] = have.get(s2[right], 0) + 1
                if have[s2[right]] == need[s2[right]]:
                    currMatching += 1
                elif have[s2[right]] == need[s2[right]] + 1:
                    currMatching -= 1
            if (right - left + 1) > len(s1):
                # move left does matching go up or down
                if s2[left] in have:
                    if have[s2[left]] == need[s2[left]]:
                        currMatching -= 1
                    elif have[s2[left]] == need[s2[left]] + 1:
                        currMatching += 1
                    have[s2[left]] -= 1
                left += 1


            if matching == currMatching:
                return True
        return matching == currMatching


            
