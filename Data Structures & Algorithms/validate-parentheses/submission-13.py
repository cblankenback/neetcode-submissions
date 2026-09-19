class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {')': '(', ']': '[', '}': '{'}
        for l in s:
            print(stack)
            if l in ['(','[','{']:
                stack.append(l)
            elif not stack or stack[-1] != lookup[l]:
                return False
            elif stack[-1] == lookup[l]:
                stack.pop()
            
        return len(stack) == 0
            