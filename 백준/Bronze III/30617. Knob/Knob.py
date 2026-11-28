import sys
input = sys.stdin.readline

n = int(input())
song = [list(map(int, input().split())) for _ in range(n)]
a = 0
if song[0][0] == song[0][1] and song[0][0] != 0:
    a += 1
for i in range(1, n):
    if song[i][0] == song[i][1] and song[i][0] != 0:
        a += 1
    if song[i][0] != 0:
        if song[i][0] == song[i-1][0]:
            a += 1
    if song[i][1] != 0:
        if song[i][1] == song[i-1][1]:
            a += 1
print(a)