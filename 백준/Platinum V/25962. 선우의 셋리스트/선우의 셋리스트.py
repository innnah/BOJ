import sys
input = sys.stdin.readline

MOD = 10**9+7
def matrix_mult(A, B):
    temp = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                temp[i][j] += (A[i][k] * B[k][j])
                temp[i][j] %= MOD
    return temp

n, m = map(int, input().split())
ret = [[0] * 5 for _ in range(5)]
mul = [[0] * 5 for _ in range(5)]
for _ in range(m):
    mul[0][int(input())-1] += 1
for i in range(1, 5):
    mul[i][i-1] = 1
for i in range(5):
    ret[i][i] = 1
while n:
    if n % 2:
        ret = matrix_mult(ret, mul)
    mul = matrix_mult(mul, mul)
    n //= 2
print(ret[0][0] % MOD)