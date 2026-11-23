import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
homework = [0 for _ in range(1001)]
l.sort(reverse=1, key=lambda x:x[1])
for i in range(n):
    for j in range(l[i][0], 0, -1):
        if not homework[j]:
            homework[j] = l[i][1]
            break
print(sum(homework))