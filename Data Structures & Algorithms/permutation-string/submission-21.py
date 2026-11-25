class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap of what is in the window
        # window size is size of s1
        # shift window if not equal otherwise return True
        if len(s1) > len(s2):
            return False
        s1hashmap = [0] * 26
        s2hashmap = [0] * 26

        for i in range(len(s1)):
            s1hashmap[ord(s1[i]) -  ord('a')] += 1
            s2hashmap[ord(s2[i]) -  ord('a')] += 1
        
        left = 0
        right = len(s1) 

        while right < len(s2):
            
            if s1hashmap == s2hashmap:
                return True
            s2hashmap[ord(s2[right]) -  ord('a')] += 1
            s2hashmap[ord(s2[left]) -  ord('a')] -= 1
            left += 1
            right += 1




        if s1hashmap == s2hashmap:
            return True
        else:
            return False

