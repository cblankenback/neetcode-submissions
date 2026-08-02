class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += str(len(s))+'#' + s
        return en

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                print(num, i)
                i+=1
            i+=1
            print("second",i, num)
            
            res.append(s[i: i + int(num)])
            i = i + int(num)
        return list(res)
