import sys
input = sys.stdin.readline
for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    v1 = d+p*n
    v2 = s*n
    if v1 > v2:
        print("do not parallelize")
    elif v1 < v2:
        print("parallelize")
    else:
        print("does not matter")