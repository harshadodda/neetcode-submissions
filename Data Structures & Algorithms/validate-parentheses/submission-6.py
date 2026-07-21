class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if (char == ")" or char == "]" or char == "}") and len(stack) == 0:
                    return False
                top = stack[-1]
                if top == "(" and char == ")":
                    stack.pop()
                elif top == "[" and char == "]":
                    stack.pop()
                elif top == "{" and char == "}":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
