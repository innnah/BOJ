import sys
input = sys.stdin.readline

def reconstruct(a, b):
    if a == -1 and b == -1:
        return ["", ""]
    v = reconstruct(trace[a][b][0], trace[a][b][1])
    if trace[a][b][0] != a:
        v[0] = s1[a] + v[0]
    if trace[a][b][1] != b:
        v[1] = s2[b] + v[1]
    return v

n = int(input())
s1 = input().rstrip()
m = int(input())
s2 = input().rstrip()
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
trace = [[[-1, -1] for _ in range(m+1)] for _ in range(n+1)]
maxval = -987654321
maxidx = [-1, -1]
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        v1 = dp[i+1][j]-2
        v2 = dp[i][j+1]-2
        v3 = dp[i+1][j+1]-2+5*(s1[i]==s2[j])
        dp[i][j] = max(0, v1, v2, v3)
        if maxval <= dp[i][j]:
            maxval = dp[i][j]
            maxidx = [i, j]
        if dp[i][j] == v1 and i+1 < n:
            trace[i][j] = [i+1, j]
        if dp[i][j] == v2 and j+1 < m:
            trace[i][j] = [i, j+1]
        if dp[i][j] == v3 and i+1 < n and j+1 < m and v3 != -2+5*(s1[i]==s2[j]):
            trace[i][j] = [i+1, j+1]
print(maxval)
print("\n".join(reconstruct(maxidx[0], maxidx[1])))