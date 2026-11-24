import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = [[], [], [], []]
for _ in range(n):
    s, k = input().rstrip().split()
    k = int(k)
    a[ord(s)-65].append(k)
for i in range(4):
    a[i].sort()
for _ in range(m):
    vals = []
    for i in range(4):
        if a[i]:
            vals.append([a[i][-1]*arr[(i+1)%4]*arr[(i+2)%4]*arr[(i+3)%4], i])
    mx = max(vals)
    for i in range(len(vals)):
        if mx == vals[i]:
            print(chr(vals[i][1]+65), a[vals[i][1]][-1])
            arr[vals[i][1]] += a[vals[i][1]][-1]
            a[vals[i][1]].pop()
            break