class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif item == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif item == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))

            elif item == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(b * a)

            else:
                stack.append(int(item))
        return stack[0]