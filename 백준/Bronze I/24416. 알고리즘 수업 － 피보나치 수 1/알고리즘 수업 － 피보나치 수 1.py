def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j]) % 1000000007
    return temp

def matrix_pow(n):
    matrix = [[1, 0], [0, 1]]
    k = 0
    tmp = [[1, 1], [1, 0]]

    while 2 ** k <= n:
        if n & (1 << k) != 0:
            matrix = matrix_mult(matrix, tmp)
        k += 1
        tmp = matrix_mult(tmp, tmp)

    return matrix

n = int(input())
print(matrix_pow(n)[1][0] % 1000000007, n-2)