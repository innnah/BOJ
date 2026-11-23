n = int(input())
ret = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if i+j+k == n and k-j >= 2 and i%2==0: ret += 1
print(ret)