n = int(input())
i, j = 1, 1
cnt = 0
while j <= n:
    s = (i+j)*(j-i+1)//2
    if s == n:
        cnt += 1
        j += 1
    elif s < n:
        j += 1
    else:
        i += 1
print(cnt)