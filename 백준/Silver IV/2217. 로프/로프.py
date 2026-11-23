import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
m = 0
for i in range(n):
    v = l.pop()
    m = max(m, v*(i+1))
print(m)