import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
stack = []
ret = 0
for i in range(n):
    if not stack:
        stack.append([l[i], 1])
    else:
        if stack[-1][0] > l[i]:
            ret += 1
            stack.append([l[i], 1])
        elif stack[-1][0] == l[i]:
            ret += stack[-1][1]
            stack[-1][1] += 1
            if len(stack) >= 2:
                ret += 1
        else:
            while stack and stack[-1][0] < l[i]:
                ret += stack.pop()[1]
            if not stack:
                stack.append([l[i], 1])
            elif stack[-1][0] == l[i]:
                ret += stack[-1][1]
                stack[-1][1] += 1
                if len(stack) >= 2:
                    ret += 1
            else:
                ret += 1
                stack.append([l[i], 1])
print(ret)