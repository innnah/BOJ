import sys

input = sys.stdin.readline

h = []
def solveStack():
    remaining = []
    h.append(0)
    ret = 0
    for i in range(len(h)):
        while remaining and h[remaining[-1]] >= h[i]:
            j = remaining[-1]
            remaining.pop()
            width = -1

            if not remaining:
                width = i
            else:
                width = i - remaining[-1] - 1
            ret = max(ret, h[j] * width)    
        remaining.append(i)

    return ret

while True:
    n, *h = list(map(int, input().split()))
    if n == 0: break
    print(solveStack())