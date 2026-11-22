import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
a = [0 for _ in range(1000001)]
for i in range(n):
    a[l[i][0]] += 1
    a[l[i][1]] -= 1
for i in range(1, 1000001):
    a[i] += a[i-1]
for i in range(1, 1000001):
    a[i] += a[i-1]
a.append(0)
i, j = -1, 0
while j <= 1000000:
    if a[j] - a[i] > k:
        i += 1
    elif a[j] - a[i] < k:
        j += 1
    else:
        print(i+1, j+1)
        sys.exit(0)
print(0, 0)