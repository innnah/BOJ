import sys
input = sys.stdin.readline

def query(v, k):
    ret = 0
    while v > 0:
        ret += dp[k][v]
        v -= (v & -v)
    return ret
def update(idx, k, num):
    while idx <= n+1:
        dp[k][idx] += num
        idx += (idx & -idx)

n = int(input())
k = 3
l = list(map(int, input().split()))[::-1]
dp = [[0] * (n+2) for _ in range(k+1)]
update(1, 0, 1)
for i in l:
    for j in range(1, k+1):
        update(i+1, j, query(i, j-1))
print(query(n+1, k))