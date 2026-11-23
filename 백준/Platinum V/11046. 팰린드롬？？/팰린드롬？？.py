import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(l[i])
    s.append(0)
n = len(s)
a = [0 for _ in range(n)]
def manachers():
    r, p = 0, 0
    for i in range(n):
        if i <= r:
            a[i] = min(a[2*p-i], r-i)
        else:
            a[i] = 0
        
        while i - a[i] - 1 >= 0 and i + a[i] + 1 < n and s[i - a[i] - 1] == s[i + a[i] + 1]:
            a[i] += 1
        
        if r < i + a[i]:
            r = i + a[i]
            p = i
manachers()
for _ in range(int(input())):
    p, q = map(int, input().split())
    p *= 2
    q *= 2
    middle = (p+q) // 2
    if a[middle-1] != 0 and (q-middle) / 2 <= (a[middle-1]) // 2:
        print(1)
    else:
        print(0)