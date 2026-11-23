import sys, bisect
input = sys.stdin.readline

n, m = map(int, input().split())
l1 = []; l2 = []
for _ in range(n):
    a, b = input().rstrip().split()
    b = int(b)
    if len(l2) != 0:
        if b != l2[-1]:
            l1.append(a)
            l2.append(b)
    else:
        l1.append(a)
        l2.append(b)
for _ in range(m):
    a = int(input())
    idx = bisect.bisect(l2, a)
    if l2[idx-1] == a:
        print(l1[idx-1])
    else:
        print(l1[idx])