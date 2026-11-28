a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
v1 = a*3+20*b+120*c
v2 = d*3+20*e+120*f
if v1 < v2:
    print("Mel")
elif v2 < v1:
    print("Max")
else:
    print("Draw")