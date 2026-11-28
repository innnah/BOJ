import sys
input = sys.stdin.readline

mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    print((pow(5, n-1, mod)*4)%mod+(n==1))