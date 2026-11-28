n, k = map(int, input().split())
ret = []
for i in range(1, n+1):
    if (i % 10) not in (k%10, (2*k)%10):
        ret.append(i)
print(len(ret))
print(*ret)