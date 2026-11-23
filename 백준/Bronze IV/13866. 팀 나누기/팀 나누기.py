l = list(map(int, input().split()))
s = sum(l)
ret = 987654321
for i in range(4):
    for j in range(i+1, 4):
        a = l[i]+l[j]
        b = s-a
        ret = min(ret, abs(a-b))
print(ret)