class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for s in s1:
            need[s] = need.get(s, 0) + 1
        matching = len(need)
        currMatching = 0
        left = 0
        have = {}
        for right in range(len(s2)):
            if matching == currMatching:
                return True
            if s2[right] in need:
                have[s2[right]] = have.get(s2[right], 0) + 1
                if have[s2[right]] == need[s2[right]]:
                    currMatching += 1
                elif have[s2[right]] == need[s2[right]] + 1:
                    currMatching -= 1
            if (right - left + 1) > len(s1):
                if s2[left] in have:
                    if have[s2[left]] == need[s2[left]]:
                        currMatching -= 1
                    elif have[s2[left]] - 1 == need[s2[left]]:
                        currMatching += 1
                    have[s2[left]] -= 1
                left +=1
        return  matching == currMatching



