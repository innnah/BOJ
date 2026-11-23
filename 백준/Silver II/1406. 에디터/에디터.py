import sys

input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = []
n = int(input())
order = []

for _ in range(n):
    order = input().rstrip().split()
    if order[0] == "L":
        if stack1: stack2.append(stack1.pop())
        else: continue
    elif order[0] == "D":
        if stack2: stack1.append(stack2.pop())
        else: continue
    elif order[0] == "B":
        if stack1: stack1.pop()
        else: continue
    else:
        stack1.append(order[1])
        
print(''.join(stack1 + list(reversed(stack2))))