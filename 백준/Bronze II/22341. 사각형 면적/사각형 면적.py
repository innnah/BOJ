n, c = map(int, input().split())
w, h = n, n
for _ in range(c):
    a, b = map(int, input().split())
    if a > h or b > w: continue
    if w * a >= h * b:
        h = a
    else:
        w = b
print(w*h)