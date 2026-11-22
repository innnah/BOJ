sum = 0
for _ in range(10):
    n = int(input())
    if sum + n == 100:
        print(100)
        break
    elif sum + n > 100:
        if 100-sum >= sum+n-100:
            print(sum+n)
        else:
            print(sum)
        break
    sum += n
else:
    print(sum)