import sys
input = sys.stdin.readline

def traceValue(a):
    return trace[a[0]][a[1]][a[2]][a[3]]

n, m = map(int, input().split())
dp = [[[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
trace = [[[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0][0] = 1
c = [-1, -1, -1, -1]
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            for v in range(m+1):
                if not (i or j or k or v): continue
                ret = 0
                if i != 0:
                    if dp[i-1][j][k][v]:
                        ret = 1
                        trace[i][j][k][v] = 1
                if j != 0:
                    if v-i >= 0:
                        if dp[i][j-1][k][v-i]:
                            ret = 1
                            trace[i][j][k][v] = 2
                if k != 0:
                    if v-i-j >= 0:
                        if dp[i][j][k-1][v-i-j]:
                            ret = 1
                            trace[i][j][k][v] = 3
                dp[i][j][k][v] = ret
                if i+j+k == n and v == m and ret:
                    c = [i, j, k, v]
if c == [-1, -1, -1, -1]:
    print(-1)
else:
    string = ""
    while c != [0, 0, 0, 0]:
        v = traceValue(c)
        if v == 1:
            string = "A" + string
            c[0] -= 1
        elif v == 2:
            string = "B" + string
            c[1] -= 1
            c[3] -= c[0]
        else:
            string = "C" + string
            c[2] -= 1
            c[3] -= c[0]+c[1]
    print(string)