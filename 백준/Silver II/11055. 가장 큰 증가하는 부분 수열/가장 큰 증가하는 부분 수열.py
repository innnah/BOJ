n = int(input())
l = list(map(int, input().split()))

d = [1]*n
d[0] = l[0]
for i in range(1,n):
    for j in range(i):
        if l[j]<l[i]:
            d[i]=max(d[i], d[j]+l[i])
        else:
            d[i]=max(d[i], l[i])

print(max(d))