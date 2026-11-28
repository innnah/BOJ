import sys
input = sys.stdin.readline
n, x = map(int, input().split())
l = list(map(int, input().split()))
ret = 10**100
for i in range(n-1):
    ret = min(ret, l[i]+l[i+1])
print(ret * x)