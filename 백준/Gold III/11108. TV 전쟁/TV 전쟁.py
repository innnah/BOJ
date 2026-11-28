import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    tmp = [list(map(int, input().split())) for _ in range(n)]
    tmp.sort()
    start = []
    lasting = []
    sat = []
    end = []
    for i in range(n):
        a, b, c = tmp[i]
        start.append(a)
        lasting.append(b)
        sat.append(c)
        end.append(a+b)
    dp = [0 for _ in range(n+1)]
    dp[0] = sat[0]
    pq = [[end[0], dp[0]]]
    val = 0
    for i in range(1, n):
        while pq and pq[0][0] <= start[i]:
            val = max(val, pq[0][1])
            heapq.heappop(pq)
        dp[i] = val + sat[i]
        heapq.heappush(pq, [end[i], dp[i]])
    print(max(dp))