import sys
input = sys.stdin.readline

n = int(input())
l = [float(input()) for _ in range(n)]
psum = 1
ret = 0
for i in range(n):
    psum *= l[i]
    ret = max(ret, psum)
    psum = max(1, psum)
print("%.3f" % ret)