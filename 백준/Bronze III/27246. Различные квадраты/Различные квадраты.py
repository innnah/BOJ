n = int(input())
cnt = 0
while n > 0:
    if (cnt+1)**2 <= n:
        cnt += 1
        n -= cnt**2
    else:
        break
print(cnt)