import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
d1 = {}
d2 = {}
for i in range(1, n+1):
    a = input().rstrip()
    d1[str(i)] = a
    d2[a] = str(i)
for _ in range(m):
    o = input().rstrip()
    if o.isalpha():
        print(d2[o] + "\n")
    else:
        print(d1[o] + "\n")