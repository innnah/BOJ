a, b, c, d = map(int, input().split())
canGrow = [i for i in range(1, a, b)]
if canGrow[-1]+b > a:
    print((len(canGrow)-1) * c * d)
else:
    print(len(canGrow) * c * d)