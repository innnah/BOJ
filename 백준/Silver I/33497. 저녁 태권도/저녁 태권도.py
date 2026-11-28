import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
ans = [["" for _ in range(m)] for _ in range(n)]
idx = 0
for i in range(m):
    for j in range(n-arr[i][0]-arr[i][1]):
        if idx >= n: break
        ans[idx][i] = "X"
        idx += 1
#print(ans)
if idx < n:
    print("NO")
    sys.exit(0)
for i in range(m):
    cnt = 0
    for j in range(n):
        if ans[j][i] != "X":
            if cnt < arr[i][0]:
                ans[j][i] = "+"
            else:
                ans[j][i] = "-"
            cnt += 1
    if cnt < arr[i][0] + arr[i][1]:
        print("NO")
        sys.exit(0)
print("YES")
for i in range(n):
    print(''.join(ans[i]))