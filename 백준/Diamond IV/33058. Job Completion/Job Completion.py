import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key = lambda x : [x[0]+x[1], x[0]])
    works = []
    t_time = 0
    ans = 0
    for i in range(n):
        heapq.heappush(works, -arr[i][1])
        while works and t_time > arr[i][0]:
            t_time += heapq.heappop(works)
        t_time += arr[i][1]
        ans = max(ans, len(works))
    print(ans)