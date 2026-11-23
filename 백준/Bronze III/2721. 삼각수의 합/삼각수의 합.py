for _ in range(int(input())):
    n = int(input())
    ret = 0
    for i in range(1, n+1):
        ret += i * (i+1) * (i+2) // 2
    print(ret)