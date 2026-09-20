class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []
        bracket = {']': '[', '}': '{', ')': '('}
        for c in s:
            print (c in bracket)
            if c in bracket:
                if stack and bracket[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            print(stack)
        return True if not stack else False