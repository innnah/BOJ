import sys

input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    tmp = input().rstrip().split()
    sub = list(map(int, tmp[1:]))
    l.append(sub + [tmp[0]])

ret = sorted(l, key = lambda x: (-x[0], x[1], -x[2], x[3]))
for i in ret:
    print(i[3])