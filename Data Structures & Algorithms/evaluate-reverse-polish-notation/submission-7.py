class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 - num1
                stack.append(res)
            elif token == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 / num1)
                stack.append(res)                
            else:
                stack.append(int(token))
        return stack.pop()