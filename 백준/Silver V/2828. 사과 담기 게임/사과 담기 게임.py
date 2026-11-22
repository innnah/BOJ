n, m = map(int, input().split())
k = int(input())
ans = 0
p = 1
for _ in range(k):
    a = int(input())
    if p <= a < p+m:
        continue
    else:
        if p < a:
            ans += a-m+1-p
            p = a-m+1
        else:
            ans += p-a
            p = a
print(ans)