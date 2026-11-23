import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())-1
    i = 2
    mod = 2
    ret = 0
    while True:
        if n < mod: break
        if n % mod == 0: ret += 1
        n -= i
        i += 1
        mod += 1
    print(ret)