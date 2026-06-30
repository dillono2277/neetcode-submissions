class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        myStack = []
        
        for c in s:
            if c == ']':
                if not myStack or myStack.pop() != '[':
                    return False
            elif c == ')':
                if not myStack or myStack.pop() != '(':
                    return False
            elif c == '}':
                if not myStack or myStack.pop() != '{':
                    return False
            else:
                myStack.append(c)
        if not myStack:
            return True
        return False
            
        