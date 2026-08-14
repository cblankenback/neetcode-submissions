class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            
            while l < r and s[l].isalnum() is False:
                l += 1
            while l < r and s[r].isalnum() is False: 
                r -= 1
            print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            
            
