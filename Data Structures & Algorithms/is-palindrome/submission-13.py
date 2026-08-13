class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not (ord('a') <= ord(s[l].lower()) <= ord('z') or ord('0') <= ord(s[l].lower()) <= ord('9')):
                l += 1
                
            while l < r and not (ord('a') <= ord(s[r].lower()) <= ord('z') or ord('0') <= ord(s[r].lower()) <= ord('9')):
                r -= 1
            print(s[r].lower(), s[l].lower() )
            if (s[l].lower()) != (s[r].lower()):
                return False
            l+=1
            r-=1
        return True