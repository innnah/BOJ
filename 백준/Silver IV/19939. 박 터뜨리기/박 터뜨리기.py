import sys

n, k = map(int, input().split())
sumToK = sum((i for i in range(1, k+1)))
if n < sumToK:
    print(-1)
    sys.exit(0)

l = [i for i in range(1, k+1)]
n -= sumToK
for i in range(len(l)):
    l[i] += n // k
n %= k
for i in range(len(l)-1, -1, -1):
    if n <= 0:
        break
    l[i] += 1
    n -= 1
print(l[-1] - l[0])