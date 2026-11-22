import sys
input = sys.stdin.readline

def modinv(x):
    return pow(x, MOD-2, MOD)

MOD = 10**9 + 7
x, n = map(int, input().split())

comb = [[0 for _ in range(n+2)] for _ in range(n+2)]
for i in range(n+2):
    comb[i][0] = 1
    comb[i][i] = 1
    for j in range(1, i):
        comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

s = [x]
for i in range(1, n+1):
    val = pow(x+1, i+1, MOD) - 1
    for j in range(i):
        val = (val - comb[i+1][j] * s[j]) % MOD
    val = (val * modinv(comb[i+1][i])) % MOD
    s.append(val)
print(s[n])