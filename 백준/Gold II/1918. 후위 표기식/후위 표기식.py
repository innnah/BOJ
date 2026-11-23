class Stack:
    def __init__(self): self.stack = []
    def __str__(self): return str(self.stack)    
    def __len__(self): return len(self.stack)  
    def push(self, value): self.stack.append(value)
    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()   
    def peek(self):
        try:
            return self.stack[-1]
        except:
            return -1

def changeExp(exp):
    stack1 = Stack()
    stack2 = Stack()
    for s in exp:
        if s in ["*", "/", "+", "-", "(", ")"]:
            if s == "(":
                stack1.push(s)
            elif s == ")":
                while len(stack1) != 0 and stack1.peek() != "(":
                    stack2.push(stack1.pop())
                stack1.pop()
            elif s == "*" or s == "/":
                while len(stack1) != 0:
                    if stack1.peek() in ["*", "/"]:
                        stack2.push(stack1.pop())
                    else:
                        break
                stack1.push(s)
            elif s == "+" or s == "-":
                while len(stack1) != 0:
                    if stack1.peek() in ["*", "/", "+", "-"]:
                        stack2.push(stack1.pop())
                    else:
                        break
                stack1.push(s)
        else:
            stack2.push(s)

    while len(stack1) != 0:
        stack2.push(stack1.pop())

    return stack2

s = list(input())
for i in changeExp(s).stack:
    print(i, end = '')