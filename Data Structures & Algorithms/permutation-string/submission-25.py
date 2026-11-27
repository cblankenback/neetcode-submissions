class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_hash = [0] * 26
        s2_hash = [0] * 26

        for i in range(len(s1)):
            s1_hash[ord(s1[i]) - ord('a')] += 1
            s2_hash[ord(s2[i]) - ord('a')] += 1
        
        matching = 0
        for i in range(26):
            if s1_hash[i] == s2_hash[i]:
                matching += 1
        
        left = 0
        right = len(s1) - 1
        while right + 1< len(s2):
            if matching == 26:
                return True
            right += 1
            right_next = ord(s2[right]) - ord('a')
            s2_hash[right_next] += 1
            if s1_hash[right_next] == s2_hash[right_next]:
                matching += 1
            elif s1_hash[right_next] == s2_hash[right_next] - 1:
                matching -= 1
            
            left_curr = ord(s2[left]) - ord('a')
            if s1_hash[left_curr] == s2_hash[left_curr]:
                matching -= 1
            elif s1_hash[left_curr] == s2_hash[left_curr] - 1:
                matching += 1
            s2_hash[left_curr] -= 1
            left += 1
        return matching == 26
            
            
            

