import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    mul = 1
    cnt = 1
    while n-mul > 0:
        n -= mul
        mul *= 2
        cnt += 1
    while cnt > 1:
        print(cnt, end = '')
        print("%018d" % n)
        cnt -= 1
        n = (n+1)//2
    print(1000000000000000001)