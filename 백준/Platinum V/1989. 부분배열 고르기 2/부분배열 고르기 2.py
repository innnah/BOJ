import sys
input = sys.stdin.readline

h = []
def solveStack():
    remaining = []
    h.append(0)
    ret = -1
    real = (-1, -1)
    for i in range(len(h)):
        while remaining and h[remaining[-1]] >= h[i]:
            j = remaining[-1]
            remaining.pop()
            width = -1

            if not remaining:
                width = psum[i]
            else:
                width = psum[i] - psum[remaining[-1]+1]
            if ret < h[j] * width:
                ret = h[j] * width
                real = ((remaining[-1] if remaining else -1) + 2, i)
            ret = max(ret, h[j] * width)
        remaining.append(i)

    return ret, real

n = int(input())
h = list(map(int, input().split()))
psum = [0 for _ in range(n+1)]
psum[1] = h[0]
for i in range(2, n+1):
    psum[i] += psum[i-1] + h[i-1]
ret = solveStack()
print(ret[0])
print(*ret[1])