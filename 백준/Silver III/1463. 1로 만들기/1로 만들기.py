n = int(input())
l = [1234567890 for _ in range(n+1)]
l[1] = 0
for i in range(2, n+1):
    if i % 3 == 0:
        l[i] = min(l[i//3]+1, l[i])
    if i % 2 == 0:
        l[i] = min(l[i//2]+1, l[i])
    l[i] = min(l[i-1]+1, l[i])
print(l[n])