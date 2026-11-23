import sys
input = sys.stdin.readline
n = int(input())
if n < 3:
    print(n)
    sys.exit(0)
a, b = 1, 2
for i in range(3, n+1):
    a, b = b, (a+b)%10007
print(b)