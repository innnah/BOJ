import sys
input = sys.stdin.readline

n = int(input())
s = set([])
for _ in range(n):
    a, b = input().rstrip().split()
    if b == "enter":
        s.add(a)
    else:
        s.remove(a)
        
for x in sorted(s, reverse = True):
    print(x)