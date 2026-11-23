import sys
m, n, q = map(int, input().split())
l = list(map(int, input().split()))
a = []
for i in range(1, m+1):
    print(f"? {i} {i}")
    sys.stdout.flush()
    v = int(input())
    if v != l[i-1]:
        a.append(v+1)
    else:
        a.append(v-1)
for _ in range(n-m):
    a.append(1)
print("!", end = ' ')
print(*a)
sys.stdout.flush()