import sys
input = sys.stdin.readline

n, y, x = map(int, input().split())
y-=1
x-=1
arr = [list(map(int, input().split())) for _ in range(n)]
flag = True
for i in range(n):
    if arr[y][x] < arr[y][i]:
        flag = False
for i in range(n):
    if arr[y][x] < arr[i][x]:
        flag = False
if flag:
    print("HAPPY")
else:
    print("ANGRY")