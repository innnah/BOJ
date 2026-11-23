import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ret = 0
for i in range(n):
    if a[i] <= b[i]:
        ret += 1
print(ret)