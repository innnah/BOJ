n = int(input())
if n < 5:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(-1)
else:
    cnt5 = n // 5
    tmp = n % 5
    
    if tmp == 0:
        print(cnt5)
    elif tmp % 2 == 0:
        print(cnt5 + tmp // 2)
    else:
        print(cnt5 - 1 + ((tmp + 5) // 2))