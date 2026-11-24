import sys
input = sys.stdin.readline

INF = 987654322
def dpf(s, e, h):
    if e-s <= 0: return 0
    if dp[s][e][h] != -1: return dp[s][e][h]
    b, w = arr[s] == 1, arr[s] == 0
    ret = INF
    for i in range(s+1, e+1):
        b += arr[i] == 1
        w += arr[i] == 0
        if b == w and arr[s] ^ arr[i]:
            for j in range(min((i-s-1)//2, (h+INF)%INF - 1)+1):
                cand = dpf(s+1, i-1, j)+dpf(i+1, e, h)+2*(j+1)+i-s
                if ret > cand:
                    ret = cand
                    trace[s][e][h] = [s, i, j]
    dp[s][e][h] = ret
    return ret
def reconstruct(s, e, h):
    if e-s <= 0:
        return
    t = trace[s][e][h]
    print(t[0]+1, t[1]+1)
    reconstruct(t[0]+1, t[1]-1, t[2])
    reconstruct(t[1]+1, e, h)

n = int(input())
arr = list(map(int, list(input().rstrip())))
dp = [[[-1 for _ in range(n//2+10)] for _ in range(n)] for _ in range(n)]
trace = [[[[-1, -1, -1] for _ in range(n//2+10)] for _ in range(n)] for _ in range(n)]
print(dpf(0, n-1, -1))
reconstruct(0, n-1, -1)