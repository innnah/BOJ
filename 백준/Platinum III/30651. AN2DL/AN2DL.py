import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
res = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    pq = []
    for j in range(m):
        heapq.heappush(pq, (-arr[i][j], j))
        while pq[0][1] < j-c+1:
            heapq.heappop(pq)
        res[i][j] = -pq[0][0]
res2 = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    pq = []
    for j in range(n):
        heapq.heappush(pq, (-res[j][i], j))
        while pq[0][1] < j-r+1:
            heapq.heappop(pq)
        res2[j][i] = -pq[0][0]
for i in range(r-1, n):
    for j in range(c-1, m):
        print(f"{res2[i][j]} ")
    print("\n")