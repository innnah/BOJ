import sys
input = sys.stdin.readline
l = [0, 1]
for i in range(2, 10001):
    l.append(l[i-1] + l[i-2])
for i in range(int(input())):
    n, p = map(int, input().split())
    print(f"Case #{i+1}: {l[n]%p}")