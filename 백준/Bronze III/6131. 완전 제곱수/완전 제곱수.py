n = int(input())
ret = 0
for i in range(1, 501):
    for j in range(i+1, 501):
        if j*j-i*i == n: ret += 1
print(ret)