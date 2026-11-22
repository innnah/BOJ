import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a-1] += 1
    cnt[b-1] += 1
for i in cnt:
    print(i)