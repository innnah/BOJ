import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
qs = [[0 for _ in range(arr[i])] for i in range(n)]
for _ in range(2):
    for i in range(n):
        s = len(qs[i])
        for j in range(s-1):
            heapq.heappush(qs[(i+s-1-j)%n], heapq.heappop(qs[i])+s-1-j)
ret = 0
for i in range(n):
    ret += heapq.heappop(qs[i])**2
print(ret)