class Solution:
    def isValid(self, s: str) -> bool:
        # '(', ')', '{', '}', '[' and ']'.
        stack = []
        for paran in s:
            # open braket
            if paran == '(' or paran == '{' or paran == '[':
                stack.append(paran) # } -> (, { -> (
            # closed braket
            else:
                if len(stack) == 0:
                    return False
                if paran == ')' and stack[-1] == '(':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif paran == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False