import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
ret = 0
cur = l[0]
for i in range(1, n):
    if l[i-1] != l[i]-1:
        ret += cur
        cur = l[i]
ret += cur
print(ret)