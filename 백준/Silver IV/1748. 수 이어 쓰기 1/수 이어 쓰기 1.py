n = int(input())
cnt = 1
ret = 0
while 10 ** cnt <= n:
    ret += cnt * (10 ** cnt - 10 ** (cnt-1) - 1) + cnt + 1
    cnt += 1
print(ret + cnt * (n - 10 ** (cnt-1)) + 1)