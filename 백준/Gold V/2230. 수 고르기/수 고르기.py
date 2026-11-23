import sys

n, m = map(int, sys.stdin.readline().split())
numlist = [0] * n
for i in range(n):
    numlist[i] = int(sys.stdin.readline().rstrip())
numlist.sort()

left, right = 0, 1
ans = sys.maxsize

while left < n and right < n:
    tmp = numlist[right] - numlist[left]
    if tmp == m:
        print(m)
        exit(0)
    if tmp < m:
        right += 1
        continue
    left += 1
    ans = min(ans, tmp)
print(ans)