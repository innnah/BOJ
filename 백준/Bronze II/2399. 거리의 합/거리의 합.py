n = int(input())
l = list(map(int, input().split()))
ret = 0
for i in range(n):
    for j in range(n):
        ret += abs(l[i]-l[j])
print(ret)