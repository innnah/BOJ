def exGCD(a, b):
    tmp = a
    x0,x1,y0,y1=1,0,0,1
    while b != 0:
        n, a, b = a//b, b, a%b
        x0, x1 = x1, x0-n*x1
        y0, y1 = y1, y0-n*y1

    return (y0 + tmp) % tmp

n, a = map(int, input().split())
print(n-a, end = ' ')
v = exGCD(n, a)
if (a*v)%n != 1:
    print(-1)
else:
    print(v)