import sys, bisect
input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
plus = [sum(i) for i in xy]
minus = [xy[i][0]-xy[i][1] for i in range(n)]
plus.sort()
minus.sort()
plus2 = [plus[0]]
minus2 = [minus[0]]
for i in range(1, n):
    if plus[i] != plus[i-1]:
        plus2.append(plus[i])
    if minus[i] != minus[i-1]:
        minus2.append(minus[i])

ans = 0
for i in range(len(minus2)):
    idx2 = bisect.bisect(plus2, minus2[i])
    ans += len(plus2)-idx2

merge = set(plus2+minus2)
ans += len(merge)

print(ans)