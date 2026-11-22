import sys
input = sys.stdin.readline

def exGCD(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        n, a, b = a//b, b, a%b
        x0, x1 = x1, x0-n*x1
        y0, y1 = y1, y0-n*y1
    return [x0, y0, a]
for _ in range(int(input())):
    k, c = map(int, input().split())
    ret = exGCD(k, c)
    if ret[2] != 1:
        print("IMPOSSIBLE")
        continue
    while 1:
        if ret[0] < 0 and ret[1] > 0:
            break
        ret[0] -= c
        ret[1] += k
    if ret[1] > 10**9:
        print("IMPOSSIBLE")
    else:
        print(ret[1])