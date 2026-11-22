k = int(input())
n = min(k, 10**6)
phi = [i for i in range(n+1)]
for i in range(2, n+1):
    if phi[i] == i:
        for j in range(i, n+1, i):
            phi[j] = phi[j] - phi[j] // i
for i in range(n+1):
    if phi[i] * i == k:
        print(i)
        break
else:
    print(-1)