import sys
input = sys.stdin.readline

MOD = 5000000
def query(v, k):
    ret = 0
    while v > 0:
        ret += dp[k][v]
        ret %= MOD
        v -= (v & -v)
    return ret
def update(idx, k, num):
    while idx <= n+1:
        dp[k][idx] += num
        dp[k][idx] %= MOD
        idx += (idx & -idx)

n, k = map(int, input().split())
l = list(map(int, input().split()))
tmp = sorted(list(set(l)))
dic = {tmp[i] : i+1 for i in range(len(tmp))}
l = [dic[i] for i in l]
dp = [[0] * (n+2) for _ in range(k+1)]
update(1, 0, 1)
for i in l:
    for j in range(1, k+1):
        update(i+1, j, query(i, j-1))
print(query(n+1, k))