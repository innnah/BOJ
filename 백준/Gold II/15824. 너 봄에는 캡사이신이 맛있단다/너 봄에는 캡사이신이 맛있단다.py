import sys
input = sys.stdin.readline

MOD = 10**9+7
n = int(input())
l = list(sorted(map(int, input().split())))
ret = 0
for i in range(n):
    ret += (l[i] * (pow(2, i, MOD) - pow(2, n-i-1, MOD))) % MOD
print(ret % MOD)