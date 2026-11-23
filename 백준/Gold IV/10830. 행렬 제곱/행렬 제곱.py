def matrix_mult(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000
    return C

def pow(A, b):
    if b == 1: return A
    if b % 2 == 0: 
        half = pow(A, b // 2)
        return matrix_mult(half, half)
    return matrix_mult(pow(A, b-1), A)

a, b = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(a)]
ret = pow(l, b)
for i in ret:
    for j in i:
        print(j % 1000, end = ' ')
    print()