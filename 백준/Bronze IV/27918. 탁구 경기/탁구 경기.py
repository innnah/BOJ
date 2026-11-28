import sys
input=sys.stdin.readline
n = int(input())
a, b = 0, 0
for _ in range(n):
    t = input().rstrip()
    if t == 'D':
        a += 1
    else:
        b += 1
    if abs(a-b) >= 2:
        break
print(f"{a}:{b}")