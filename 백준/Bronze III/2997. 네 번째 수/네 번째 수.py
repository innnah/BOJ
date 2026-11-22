l = list(sorted(map(int, input().split())))
a, b, c = l
if a-b == b-c:
    print(c+c-b)
else:
    if a-b == (b-c)*2:
        print((a+b)//2)
    else:
        print((b+c)//2)