n = int(input())
mod = 1000000009
ans = 1
for i in range(1, n+1):
    ans *= 2*i-1
    ans %= mod
print(ans)