for _ in range(int(input())):
    n, d = map(int, input().split())
    ret = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        ret += a*(b/c)>=d
    print(ret)