class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] != i:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0