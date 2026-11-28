import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1, n):
    si = str(i)
    if '50' in si:
        cnt += 2
    else:
        cnt += 1
print(cnt+1)