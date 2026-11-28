import sys, bisect, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    event = [[i, 0, 0, 0] for i in arr]
    for _ in range(m):
        a, b, c = map(int, input().split())
        exist = bisect.bisect(arr, b) - bisect.bisect_left(arr, a)
        event.append([a, -1, b, exist-c])
    event.sort()
    pq = []
    ans = 0
    for l, i, r, t in event:
        if i == -1:
            heapq.heappush(pq, [ans+t, r])
        else:
            while pq and pq[0][1] < l:
                heapq.heappop(pq)
            if not pq or pq[0][0] > ans:
                ans += 1
    print(ans)