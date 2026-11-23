import sys
input = sys.stdin.readline

n = int(input())
l = [(int(input()), i) for i in range(n)]
l.sort()
ret = 0
for i in range(n):
    ret = max(ret, l[i][1] - i)
print(ret+1)