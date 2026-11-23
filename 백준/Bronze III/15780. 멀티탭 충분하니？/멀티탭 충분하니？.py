n, m = map(int, input().split())
l = list(map(int, input().split()))
s = 0
for i in range(m):
    s += (l[i]+1)//2
print("YES" if s >= n else "NO")