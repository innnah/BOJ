import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))

maxA = 0
maxB = 0
a = 1
b = 1

for i in range(n-1):
    if l[i] <= l[i+1]:
        a += 1
    else:
        maxA = max(maxA, a)
        a = 1
    if l[i] >= l[i+1]:
        b += 1
    else:
        maxB = max(maxB, b)
        b = 1
maxA = max(maxA, a)
maxB = max(maxB, b)
print(max(maxA, maxB))