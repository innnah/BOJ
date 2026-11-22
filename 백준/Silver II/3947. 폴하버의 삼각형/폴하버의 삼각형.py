import sys, fractions as frac
input = sys.stdin.readline

triangle = [[0 for _ in range(401)] for _ in range(401)]
triangle[0][0] = frac.Fraction(1, 1)
for i in range(1, 401):
    for j in range(1, i+1):
        triangle[i][j] = frac.Fraction(i, j+1) * triangle[i-1][j-1]
    triangle[i][0] = 1 - sum(triangle[i][1:])
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(triangle[n][k-1])