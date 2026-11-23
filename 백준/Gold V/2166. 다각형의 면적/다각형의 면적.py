import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
ret = 0
for i in range(n):
    ret += l[i][0] * l[(i+1)%n][1]
for i in range(n):
    ret -= l[i][1] * l[(i+1)%n][0]
print(round(abs(ret) / 2, 1))