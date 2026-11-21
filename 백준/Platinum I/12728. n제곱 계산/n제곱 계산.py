import sys

input = sys.stdin.readline

mod = 1000
def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j]) % mod
    return temp

def matrix_pow(A, n):
    ret = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            ret = matrix_mult(ret, A)
        A = matrix_mult(A, A)
        n >>= 1
    return ret

for i in range(1, int(input())+1):
    print(f"Case #{i}: ", end = '')
    n = int(input())
    mat = [[6, -4], [1, 0]]
    ret = matrix_pow(mat, n)
    print("%03d" % ((ret[1][0] * 6 + ret[1][1] * 2 + 9999) % mod))