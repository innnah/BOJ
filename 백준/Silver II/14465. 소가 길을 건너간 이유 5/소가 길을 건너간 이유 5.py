import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
l = [int(input()) for _ in range(b)]
enabled = [0 for _ in range(n)]
for i in l:
    enabled[i-1] = 1
for i in range(1, n):
    enabled[i] += enabled[i-1]
enabled.append(0)
ret = n+1
for i in range(n-k+1):
    ret = min(ret, enabled[i+k-1] - enabled[i-1])
print(ret)