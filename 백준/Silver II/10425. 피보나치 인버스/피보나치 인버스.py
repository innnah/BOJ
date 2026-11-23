import sys

input = sys.stdin.readline

l = {}
l[0] = p1 = 0
l[1] = p2 = 1
for i in range(2, 100001):
    tmp = str(p1 + p2)[-20:]
    l[int(tmp)] = i
    p1, p2 = p2, int(tmp)

for _ in range(int(input())):
    n = int(input().rstrip()[-20:])
    print(l[n])