def power(x, y, mod):
    res = 1
    x %= mod
    while y:
        if y % 2:  res = (res * x) % mod
        y //= 2
        x = (x*x) % mod
    
    return res

for _ in range(int(input())):
    a, b = map(int, input().split())
    ret = power(a, b, 10)
    if ret != 0:
        print(ret)
    else:
        print(10)