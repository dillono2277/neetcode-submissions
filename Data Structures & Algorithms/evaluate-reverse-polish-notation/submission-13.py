class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        total = 0

        # loop through tokens, while not '+', '-', '*', and '/', add to stack
        # if its an op, do the operation, then add total to stack , repeat
        for token in tokens:
            if token == '+':
                total = 0
                count = 0
                while len(numStack) > 0 and count < 2:
                    total = total + numStack.pop()
                    count += 1
                numStack.append(total)
            elif token == '-':
                temp = numStack.pop()
                total = numStack.pop() - temp
                numStack.append(total)
            elif token == '*':
                total = 1
                count = 0
                while len(numStack) > 0 and count < 2:
                    total = total * numStack.pop()
                    count += 1
                numStack.append(total)
            elif token == '/':
                temp = numStack.pop()
                total = int(numStack.pop() / temp)
                numStack.append(total)
            else:
                numStack.append(int(token))
        return numStack.pop()


            
            
        