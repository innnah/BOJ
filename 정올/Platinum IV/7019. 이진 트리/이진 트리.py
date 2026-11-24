import sys
input = sys.stdin.readline

MOD = 10**9+7
n = int(input())
a = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
s = [0 for _ in range(n+1)]
le = [0 for _ in range(n+1)]
ri = [0 for _ in range(n+1)]
leafs = [0 for _ in range(n+1)]
s[0] = le[0] = ri[0] = leafs[0] = 1
for i in range(1, n+1):
    left, right = a[i]
    s[i] = s[left] + s[right] + leafs[right] * ri[left] + leafs[left] * le[right] - 1
    le[i] = le[left] + le[right] + leafs[right] - 1
    ri[i] = ri[left] + ri[right] + leafs[left] - 1
    leafs[i] = leafs[left] + leafs[right]
    s[i] %= MOD; le[i] %= MOD; ri[i] %= MOD; leafs[i] %= MOD
    print(s[i])