import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = input().rstrip()
stack = []
for i in range(n):
    while k > 0 and stack and stack[-1] < p[i]:
        stack.pop()
        k -= 1
    stack.append(p[i])
print(''.join(stack[:len(stack)-k]))