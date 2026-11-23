import sys

sys.setrecursionlimit(987654321)

mod = 1000
bases = [[[1, 0], [0, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]], \
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], \
    [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]]

def matrix_plus(A, B):
    C = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j] = (A[i][j] + B[i][j])

    return C

def matrix_mult(A, B):
    temp = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                temp[i][j] += (A[i][k] * B[k][j]) % mod
    return temp

def matrix_pow(A, n):
    ret = bases[len(A)-2]
    while n:
        if n & 1:
            ret = matrix_mult(ret, A)
        A = matrix_mult(A, A)
        n >>= 1
    return ret

def S(A, b):
    if b == 1: return A
    ret = matrix_mult(S(A, b >> 1), matrix_plus(I, matrix_pow(A, b >> 1)))
    if b & 1: ret = matrix_plus(ret, matrix_pow(A, b))
    return ret

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
I = bases[n-2]
A = S(A, b)
for i in range(n):
    for j in range(n):
        A[i][j] %= mod
        print(A[i][j], end = ' ')
    print()