n = int(input())
l = list(map(int, input().split()))
cnt = 1
ret = 0
for i in l:
    if i == cnt:
        cnt += 1
    else:
        ret += 1
print(ret)