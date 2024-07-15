class Stack:
    # Stack implementation
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        
    def clear(self):
        self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self) -> str:
        return str(self.stack)

class Solution:
    def isValid(self, s: str) -> bool:
        # The values of the dictionary are the opening brackets
        # and the keys are the closing ones

        map = {')' : '(', ']' : '[', '}': '{'}
        my_stack = Stack()

        for char in s:
            if char in map.values():
                my_stack.push(char)
            elif char in map.keys():
                if my_stack.peek() == map.get(char):
                    my_stack.pop()
                else:
                    return False
                
        return my_stack.is_empty()