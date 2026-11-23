import sys

n, m = map(int, input().split())
numlist = list(map(int, input().split()))

totals = [0] * (n+1)

for i in range(1,n+1):
    totals[i] = totals[i-1] + numlist[i-1]
    
ret = sys.maxsize
start = 0
end = 1

while start != n:
    if totals[end] - totals[start] >= m:
        if end - start < ret:
            ret = end - start
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1

if ret == sys.maxsize:
    print(0)
else:
    print(ret)