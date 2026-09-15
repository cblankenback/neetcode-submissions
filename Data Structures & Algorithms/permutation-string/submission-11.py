class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1hash = [0] * 26
        s2hash = [0] * 26
        for i in range(len(s1)):
            s1hash[(ord(s1[i])-ord('a'))] += 1
            s2hash[(ord(s2[i])-ord('a'))] += 1
        
        matching = 0
        for i in range(26):
            matching += (1 if s1hash[i] == s2hash[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matching == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2hash[index] += 1
            if s2hash[index] == s1hash[index]:
                matching += 1
            elif s2hash[index] == s1hash[index] + 1:
                matching -= 1
            index = ord(s2[l]) - ord('a')
            s2hash[index] -= 1
            if s2hash[index] == s1hash[index]:
                matching += 1
            elif s2hash[index] == s1hash[index] - 1:
                matching -= 1
            l += 1
        return matching == 26

