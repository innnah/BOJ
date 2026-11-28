a, b = map(int, input().split())
k, x = map(int, input().split())
c, d = k-x, k+x
if b < c or d < a:
    print("IMPOSSIBLE")
else:
    le, ri = max(a, c), min(b, d)
    print(ri-le+1)