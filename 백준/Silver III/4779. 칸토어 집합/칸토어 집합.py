try:
    while True:
        n = int(input())
        s = "-"
        tmp = s
        cnt = 1
        for i in range(n):
            s += " " * cnt
            s += tmp
            tmp = s
            cnt *= 3
        print(s)
except:
    exit()