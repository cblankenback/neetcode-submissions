class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        
        left = 0
        right = len(s1) - 1

        s1hash = [0] * 26
        s2hash = [0] * 26

        for i in range(len(s1)):
            s1hash[ord(s1[i]) - ord('a')] += 1
            s2hash[ord(s2[i]) - ord('a')] += 1
        matching = 0
        for i in range(26):
            if s1hash[i] == s2hash[i]:
                matching += 1
        
        while right < len(s2) - 1:
            if matching == 26:
                return True
            
            right += 1
            new_right = ord(s2[right]) - ord('a')
            s2hash[new_right] += 1
            if s2hash[new_right] == s1hash[new_right]:
                matching += 1
            elif s2hash[new_right] - 1 == s1hash[new_right]:
                matching -= 1
            
            
            new_left = ord(s2[left]) - ord('a')
            s2hash[new_left] -= 1
            if s2hash[new_left] == s1hash[new_left]:
                matching += 1
            elif s2hash[new_left] + 1 == s1hash[new_left]:
                matching -= 1
            left += 1
            
        return True if matching == 26 else False


            
