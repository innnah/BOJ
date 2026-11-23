n, m = map(int, input().split())
l = list(map(int, input().split()))
ret = 1
for i in l:
    ret *= i
print(ret % m)