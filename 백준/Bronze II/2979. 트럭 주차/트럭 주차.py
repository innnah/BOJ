import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
arr = [0 for _ in range(100)]
for _ in range(3):
    x, y = map(int, input().split())
    for i in range(x, y):
        arr[i] += 1
ans = 0
for i in range(100):
    if arr[i] == 1:
        ans += a
    elif arr[i] == 2:
        ans += b * 2
    elif arr[i] == 3:
        ans += c * 3
print(ans)