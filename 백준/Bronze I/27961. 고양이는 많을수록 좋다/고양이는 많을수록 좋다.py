cnt = 1
a = 1
n = int(input())
if n == 0:
    print(0)
    exit(0)
while a < n:
    a *= 2
    cnt += 1
print(cnt)