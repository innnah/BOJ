import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mul = n
l = [n]
while 1:
    n = (n*mul) % m
    if n in l:
        idx = l.index(n)
        print(len(l)-idx)
        break
    l.append(n)