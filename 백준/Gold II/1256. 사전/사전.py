MAX = 10**9+10
def kth(a, b, skip):
    if b == 0: return 'a' * a
    if skip < c[a-1+b][b]:
        return 'a' + kth(a-1, b, skip)
    return 'z' + kth(a, b-1, skip - c[a-1+b][b])

n, m, k = map(int, input().split())
c = [[0] * 201 for _ in range(201)]
c[1][0] = 1
c[1][1] = 1
for i in range(2, 201):
    for j in range(i+1):
        c[i][j] = min(MAX, c[i-1][j] + c[i-1][j-1])
if c[n+m][n] < k:
    print(-1)
else:
    print(kth(n, m, k-1))