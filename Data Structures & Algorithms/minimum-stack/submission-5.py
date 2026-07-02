class MinStack:

    def __init__(self):
        self.myStack = []
        self.minStack = []
        self.minVal = float('inf')

        

    def push(self, val: int) -> None:
        self.myStack.append(val)
        self.minVal = min(val, self.minVal)
        self.minStack.append(self.minVal)
        

    def pop(self) -> None:
        self.myStack.pop()
        self.minStack.pop()
        if self.minStack:
            self.minVal = self.minStack[-1]
        else:
            self.minVal = float('inf')
        
        

    def top(self) -> int:
        return self.myStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


        
