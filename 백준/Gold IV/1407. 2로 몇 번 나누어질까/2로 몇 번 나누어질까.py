def f(n):
    cnt = n
    i = 1
    while 2**i <= n:
        cnt += (n // 2 ** i) * (2 ** (i-1))
        i += 1

    return cnt

a, b = map(int, input().split())
print(f(b)-f(a-1))