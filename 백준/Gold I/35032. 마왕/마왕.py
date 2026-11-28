import sys
input = sys.stdin.readline

n = int(input())
rects = [map(int, input().split()) for _ in range(n)]
for i in range(n):
    a, b, c = rects[i]
    rects[i] = [a-c, b-c, a+c, b+c, i+1]
rects.sort()

ans = []
for i in range(n):
    a1, b1, a2, b2, _ = rects[i]
    overlap = 0
    for j in range(len(ans)):
        c1, d1, c2, d2, _ = ans[j]
        if not (a2 < c1 or c2 < a1 or b2 < d1 or d2 < b1):
            overlap = 1
            break
    if not overlap:
        ans.append(rects[i])
print(len(ans))
for r in ans:
    print(r[4])