for _ in range(int(input())):
    a = int(input())
    ret = 0
    for i in range(1, a+1, 2):
        ret += i
    print(ret)