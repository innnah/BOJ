import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
colors = [[] for _ in range(n+1)]
for i in range(n):
    colors[arr[i][1]].append(arr[i])

ans = 0
for i in range(1, n+1):
    for j in range(len(colors[i])):
        if j == 0:
            ans += colors[i][j+1][0] - colors[i][j][0]
        elif j == len(colors[i])-1:
            ans += colors[i][j][0] - colors[i][j-1][0]
        else:
            ans += min(colors[i][j+1][0] - colors[i][j][0], colors[i][j][0] - colors[i][j-1][0])
print(ans)