import sys
input = sys.stdin.readline

n = int(input())
val = pow(2, n-1, 10000)
tmp = 0
for i in range(1, len(str(n))):
    tmp += i * (10**i - 10**(i-1))
tmp += len(str(n)) * (n - 10**(len(str(n))-1) + 1)
print((3*n-4 + (n+2)*val + tmp*(val+1)) % 10000)