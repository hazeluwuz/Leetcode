class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stack to store any integers we loop over
        stack = []
        for token in tokens:
            if token in '+-*/':
                a,b = stack.pop(), stack.pop()
            if token == "+":
                stack.append(b+a)
            elif token == "-":
                stack.append(b-a)
            elif token == "*":
                stack.append(b*a)
            elif token == "/":
                stack.append(int(b/a))
            else:
                stack.append(int(token))

        return stack[0]