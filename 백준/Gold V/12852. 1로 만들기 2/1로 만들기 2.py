n = int(input())
l = [1234567890 for _ in range(n+1)]
re = [0 for _ in range(n+1)]
l[1] = 0
for i in range(2, n+1):
    best = 1234567890
    if i % 3 == 0 and l[i//3]+1 < l[i]:
        l[i] = l[i//3]+1
        best = i//3
    if i % 2 == 0 and l[i//2]+1 < l[i]:
        l[i] = l[i//2]+1
        best = i//2
    if l[i-1]+1 < l[i]:
        l[i] = l[i-1]+1
        best = i-1
    re[i] = best
print(l[n])
idx = n
while True:
    print(idx, end = ' ')
    if idx == 1: break
    idx = re[idx]