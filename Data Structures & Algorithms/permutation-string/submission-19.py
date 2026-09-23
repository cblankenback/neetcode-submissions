class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        have = [0] * 26
        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            have[ord(s2[i]) - ord('a')] += 1
        matching = 0
        for i in range(26):
            if need[i] == have[i]:
                matching += 1
        left = 0
        for right in range(len(s1), len(s2)):
            if matching == 26:
                return True
            index = ord(s2[right]) - ord('a')
            have[index] += 1
            if have[index] == need[index]:
                matching += 1
                # 3 == 3
                # 4 == 3
            elif have[index] == need[index] + 1:
                matching -= 1
            index = ord(s2[left]) - ord('a')
            have[index] -= 1
            if have[index] == need[index]:
                matching += 1
                # 3 == 3
                # 2 == 3
            elif have[index] == need[index] - 1:
                matching -= 1
            left += 1
        return matching == 26
