import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = set([input().rstrip() for _ in range(n)])
cnt = 0
for _ in range(k):
    st = input().rstrip()
    if st in s:
        cnt += 1
print(cnt)