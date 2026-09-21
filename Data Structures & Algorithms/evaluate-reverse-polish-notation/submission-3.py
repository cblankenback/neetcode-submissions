class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for num in tokens:
            if num == '+':
                stack.append(stack.pop() + stack.pop())
                
            elif num == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif num == '*':
                stack.append(stack.pop() * stack.pop())
            elif num == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(num))
        return stack[0]