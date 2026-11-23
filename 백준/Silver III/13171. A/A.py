def power(a, b, mod):
    if b == 1: return a % mod
    if b % 2 == 1:
        ret = power(a, (b-1)//2, mod) % mod
        return (ret * ret * a) % mod
    ret = power(a, b//2, mod) % mod
    return (ret * ret) % mod

print(power(int(input()), int(input()), 1000000007))