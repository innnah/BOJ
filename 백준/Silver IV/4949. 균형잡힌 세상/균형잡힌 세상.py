import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == ".":
        break

    stack = []
    opening = '(['
    closing = ')]'
    for i in s:
        if i in opening:
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                print("no")
                break
            stack.pop()
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                print("no")
                break
            stack.pop()
    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")