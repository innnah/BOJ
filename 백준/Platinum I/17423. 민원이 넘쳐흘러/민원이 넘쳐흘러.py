import sys
input = sys.stdin.readline

def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

n = int(input())
arr = list(map(int, input().split()))
cs = [list(map(int, input().split())) for _ in range(n)]
ans = 10**100
for i in range(n):
    for j in range(i+1, n):
        ans = min(ans, dist(cs[i], cs[j])//(arr[i]+arr[j]))
print(ans)