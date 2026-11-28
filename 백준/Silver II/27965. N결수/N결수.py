import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
ret = 0
for i in range(1, n+1):
    ret = (((ret * (10 ** (int(math.log10(i))+1)))%m) + (i%m)) % m
print(ret)