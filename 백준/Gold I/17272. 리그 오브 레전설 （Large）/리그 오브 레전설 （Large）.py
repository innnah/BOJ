MOD = 1000000007
def matrix_mult(A, B):
    temp = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                temp[i][j] += (A[i][k] * B[k][j])
                temp[i][j] %= MOD
    return temp

def matrix_pow(A, n):
    result = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        result[i][i] = 1
    while n:
        if n % 2:
            result = matrix_mult(result, A)
        A = matrix_mult(A, A)
        n //= 2
    return result

n, m = map(int, input().split())
if n < m: print(1)
elif n == m: print(2)
elif n == m+1: print(3)
else:
    mult = [[0] * (m+1) for _ in range(m+1)]
    for i in range(1, m+1):
        mult[i][i-1] = 1
    mult[0][0] = 1
    mult[0][m-1] += 1
    a = [[0] * (m+1) for _ in range(m+1)]
    for i in range(2, m+1):
        a[i][-1] = 1
    a[0][-1] = 3
    a[1][-1] = 2
    print(matrix_mult(matrix_pow(mult, n-m-1), a)[0][-1])