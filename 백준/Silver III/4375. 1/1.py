while True:
    try:
        n = int(input())
    except:
        break
    i = 11
    num = 2
    if n == 1:
        print(1)
    else:
        while i % n:
            i %= n
            i = i * 10 + 1
            num += 1
        print(num)