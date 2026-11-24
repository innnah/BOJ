import sys
input = sys.stdin.readline

def dpf(s, e):
    if s == e:
        return 0
    if dp[s][e] != -1: return dp[s][e]
    ret = 99999999
    for i in range(s, e):
        ret = min(ret, dpf(s, i)+dpf(i+1, e)+(arr[s]!=arr[i+1]))
    dp[s][e] = ret
    return ret

n, m = map(int, input().split())
l = list(map(int, input().split()))
arr = []
for i in range(n-1):
    if l[i] != l[i+1]:
        arr.append(l[i])
arr.append(l[-1])
n = len(arr)
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
print(dpf(0, n-1))