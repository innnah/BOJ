n = int(input())
l = list(map(int, input().split()))
k = int(input())
ret = 0
for i in l:
    if i == k:
        ret += 1
print(ret)