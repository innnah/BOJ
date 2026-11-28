n, m = map(int, input().split())
MOD = 14579
ret = 1
for i in range(n, m+1):
    ret *= i*(i+1)//2
    ret %= MOD
print(ret)