while 1:
    n = int(input())
    if n == 0: break
    ret = 0
    for i in range(1, n+1):
        ret += i*i
    print(ret)