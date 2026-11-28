n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
all = sum(l)
per1 = m // all
for i in l:
    print(per1 * i)