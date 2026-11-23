import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = 2
l = [1 for _ in range(n+1)]
while 1:
    if not l[num]:
        num += 1
        continue
    m -= 1
    l[num] = 0
    if not m:
        print(num)
        break
    for i in range(num**2, n+1, num):
        if l[i]:
            l[i] = 0
            m -= 1
        if not m:
            print(i)
            sys.exit(0)
    num += 1