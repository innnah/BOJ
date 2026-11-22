import sys, fractions
input = sys.stdin.readline

n = int(input())
h = [-1 for _ in range(5001)]
arr = [list(map(int, input().split())) for _ in range(n+1)]
arr.sort()
for i in range(n+1):
    a, b = arr[i]
    h[a] = b
for i in range(n):
    acc = fractions.Fraction(arr[i+1][1]-arr[i][1], arr[i+1][0]-arr[i][0])
    for j in range(arr[i][0]+1, arr[i+1][0]):
        h[j] = h[j-1] + acc
x, y = map(int, input().split())
print(fractions.Fraction(abs(h[y]-h[x]), (y-x)))