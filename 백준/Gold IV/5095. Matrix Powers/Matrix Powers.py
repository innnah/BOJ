import sys

input = sys.stdin.readline
print = sys.stdout.write

def matrix_mult(A, B):
    temp = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                temp[i][j] += (A[i][k] * B[k][j]) % m
    return temp

def matrix_pow(A, n):
    ret = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        ret[i][i] = 1
    while n:
        if n & 1:
            ret = matrix_mult(ret, A)
        A = matrix_mult(A, A)
        n >>= 1
    return ret

while True:
    n, m, p = map(int, input().split())
    if (n,m,p) == (0,0,0): break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ret = matrix_pow(matrix, p)
    for i in range(n):
        for j in range(n):
            ret[i][j] %= m
            print(str(ret[i][j]) + ' ') 
        print("\n")
    print("\n")