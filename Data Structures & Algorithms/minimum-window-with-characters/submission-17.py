class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = {}
        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1
        
        matching  = len(need)
        currMatching = 0
        left = 0
        minLength = float('inf')
        res = [-1, -1]
        window = {}
        for right in range(len(s)):
            if s[right] in need:
                window[s[right]] = window.get(s[right], 0 ) + 1
                if window[s[right]] == need[s[right]]:
                    currMatching += 1
            while currMatching == matching:
                #shift l over
                # update currMatching if its not matching anymore
                # we alos need to keep track of res
                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] == need[s[left]] - 1:
                        currMatching -= 1
                
                if minLength > right - left + 1:
                    minLength = right - left + 1
                    res = [left, right+1]
                left += 1
        
        return s[res[0]:res[1]] if res[1] != -1 else ""

            






