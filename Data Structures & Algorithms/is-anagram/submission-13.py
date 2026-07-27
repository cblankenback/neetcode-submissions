class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1 = {}
        hashmap2 = {}
        for letter in s:
            hashmap1[letter] = hashmap1.get(letter,0) + 1
        for letter in t:
            hashmap2[letter] = hashmap2.get(letter,0) + 1
        if hashmap1 == hashmap2:
            return True
        return False