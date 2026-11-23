import sys
input = sys.stdin.readline

MOD = 10**8+7
def matrix_mult(A, B):
    a = len(A)
    temp = [[0] * a for _ in range(a)]
    for i in range(a):
        for j in range(a):
            for k in range(a):
                temp[i][j] += A[i][k] * B[k][j] % MOD
    return temp

for _ in range(int(input())):
    m, n = map(int, input().split())
    if m >= n:
        print(1)
        continue
    mul = [[0] * (m+1) for _ in range(m+1)]
    ret = [[0] * (m+1) for _ in range(m+1)]
    mul[0][0] += 1
    mul[0][-1] += 1
    for i in range(m+1):
        ret[i][i] += 1
        if i != m:
            mul[i+1][i] += 1
    while n:
        if n % 2:
            ret = matrix_mult(ret, mul)
        mul = matrix_mult(mul, mul)
        n //= 2
    print(ret[0][0] % MOD)