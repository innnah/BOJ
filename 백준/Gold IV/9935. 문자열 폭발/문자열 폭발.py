import sys

input = sys.stdin.readline

s = input().rstrip()
explode_s = input().rstrip()
lastC = explode_s[-1]
stack = []
size = len(explode_s)

for c in s:
    stack.append(c)
    if c == lastC and ''.join(stack[-size:]) == explode_s:
        del stack[-size:]

ret = ''.join(stack)
if ret == '':
    print("FRULA")
else:
    print(ret)