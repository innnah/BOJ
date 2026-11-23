import sys, decimal, math
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
k = int(input())
a = sum(l)
divide = decimal.Decimal(math.factorial(a) // math.factorial(a-k))
number = decimal.Decimal(0)
for i in l:
    if i >= k:
        number += decimal.Decimal(math.factorial(i) // math.factorial(i-k))
print(number/divide)