mod = 1000000000

def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j]) % mod
    return temp

def matrix_pow(n, M):
    if n == 1:
        return M
    if n % 2 == 0:
        temp = matrix_pow(n//2, M)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(n-1, M)
        return matrix_mult(temp, M)

def fib2(n):
    A = [[1, 1], [1, 0]]
    return matrix_pow(n-1, A)[0][0]

a, b = map(int, input().split())
print((fib2(b+2)-fib2(a+1))%mod)