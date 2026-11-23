import sys

input = sys.stdin.readline
print = sys.stdout.write

mod = 1000000007

def bino(n, k):
    def pow(n, k):
        if k == 1:
            return n
        pow_half = pow(n, k//2)
        if k % 2 == 0:
            return (pow_half ** 2) % mod
        else:
            return (pow_half ** 2 * n) % mod

    def inverse(n):
        return pow(factorial[n], mod-2)

    return factorial[n] * inverse(n-k) * inverse(k) % mod

n, m = map(int, input().split())
factorial = [1] * (n+1)
for idx in range(2, n+1):
    factorial[idx] = (factorial[idx-1] * idx) % mod
print(str(bino(n, m) % mod) + "\n")