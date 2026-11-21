import sys
input = sys.stdin.readline

def f(x, mod):
    if x == 0 or mod == 1: return 1
    v = pow(b, f(x-1, phi[mod]), mod)
    if v == 0: return mod
    return v

n = 10000000
phi = [i for i in range(n+1)]
phi[1] = 0
for i in range(2, n+1):
    if phi[i] == i:
        for j in range(i, n+1, i):
            phi[j] = phi[j] - phi[j] // i
while True:
    b = int(input())
    if b == 0: break
    i = int(input())
    n = int(input())
    ret = str(f(i, 10**n)%(10**n))
    print("0" * (n-len(ret)) + ret)