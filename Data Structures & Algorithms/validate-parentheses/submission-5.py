class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)
        stack = []
        for char in chars:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char==')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                    
                elif char=='}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif char==']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        else:
            return True