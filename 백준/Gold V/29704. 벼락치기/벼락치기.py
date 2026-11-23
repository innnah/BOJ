import sys
sys.setrecursionlimit(1200000)
input = sys.stdin.readline

def dpf(prob, days):
    if days > m: return 1203981820498120398102948010
    if prob == n: return 0
    if days == m: return dpf(prob+1, days)+probs[prob][1]
    if dp[prob][days] != -1: return dp[prob][days]
    dp[prob][days] = min(dpf(prob+1, days+probs[prob][0]), dpf(prob+1, days)+probs[prob][1])
    return dp[prob][days]

n, m = map(int, input().split())
probs = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (m+1) for _ in range(n+1)]
print(dpf(0, 0))