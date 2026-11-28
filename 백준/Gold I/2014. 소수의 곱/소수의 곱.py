import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
primes = list(map(int, input().split()))
pq = [1]
for _ in range(m):
    v = heapq.heappop(pq)
    for i in range(n):
        heapq.heappush(pq, v * primes[i])
        if v % primes[i] == 0:
            break
print(heapq.heappop(pq))