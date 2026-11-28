import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    ret = 0
    for i in range(1, n):
        for j in range(i+1, n):
            if (i*i+j*j+m) % (i*j) == 0:
                ret += 1
    print(ret)