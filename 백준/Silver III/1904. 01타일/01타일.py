import sys
input = sys.stdin.readline
n = int(input())
a, b = 1, 1
MOD = 15746
for _ in range(n): a, b = b, (a+b) % MOD
print(a)