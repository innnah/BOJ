n = int(input())
cnt = 0
for i in range(1, n+1):
    a = i
    sum = 0
    while a > 0:
        sum += a%10
        a //= 10
    if i % sum == 0:
        cnt += 1
print(cnt)