n = int(input())
cnt = 1
ret = 0
while n > 0:
    if cnt > n: cnt = 1
    n -= cnt
    cnt += 1
    ret += 1
print(ret)