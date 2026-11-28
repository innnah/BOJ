import sys
input = sys.stdin.readline

n, birch = input().rstrip().split()
n = int(n)
ret = 0
for _ in range(n):
    a, b = input().rstrip().split()
    b = int(b)
    a = a.split("_")
    if birch in a:
        ret += b
print(ret)