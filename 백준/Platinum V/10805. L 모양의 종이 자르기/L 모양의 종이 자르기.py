def solveRectangle(h, w):
    if h == 1: return w
    if w == 1: return h
    if h == w: return 1
    if dp_rect[h][w] != 0: return dp_rect[h][w]
    ret = 10**100
    for i in range(1, h):
        ret = min(ret, solveRectangle(i, w)+solveRectangle(h-i, w))
    for i in range(1, w):
        ret = min(ret, solveRectangle(h, i)+solveRectangle(h, w-i))
    dp_rect[h][w] = ret
    return ret
def dpf(h1, w1, h2, w2):
    if w2 == 0 and h2 == 0:
        return solveRectangle(h1, w1)
    if dp[h1][w1][h2][w2] != 0: return dp[h1][w1][h2][w2]
    ret = 10**100
    for i in range(1, w1):
        if i < w2:
            ret = min(ret, solveRectangle(h1-h2, i)+dpf(h1, w1-i, h2, w2-i))
        elif i == w2:
            ret = min(ret, solveRectangle(h1-h2, w2)+solveRectangle(h1, w1-w2))
        else:
            ret = min(ret, solveRectangle(h1, w1-i)+dpf(h1, i, h2, w2))
    for i in range(1, h1):
        if i < h2:
            ret = min(ret, solveRectangle(i, w1-w2)+dpf(h1-i, w1, h2-i, w2))
        elif i == h2:
            ret = min(ret, solveRectangle(h2, w1-w2)+solveRectangle(h1-h2, w1))
        else:
            ret = min(ret, solveRectangle(h1-i, w1)+dpf(i, w1, h2, w2))
    dp[h1][w1][h2][w2] = ret
    return ret

a, b, c, d = map(int, input().split())
dp = [[[[0] * (d+1) for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
dp_rect = [[0] * (b+1) for _ in range(a+1)]
print(dpf(a, b, c, d))