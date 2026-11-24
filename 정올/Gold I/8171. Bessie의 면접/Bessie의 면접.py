import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pq = []
arr2 = []
for i in range(m):
    heapq.heappush(pq, (arr[i], i, i))
cur = m
while cur < n:
    val, idx, f = heapq.heappop(pq)
    cnt = 1
    farmers = [f]
    while pq and val == pq[0][0]:
        farmers.append(heapq.heappop(pq)[2])
        cnt += 1
    for i in range(cnt):
        heapq.heappush(pq, (val+arr[cur+i], cur+i, farmers[i]))
    cur += cnt
    arr2.append(farmers)
ans1, _, f = heapq.heappop(pq)
print(ans1)

ans2 = [0 for _ in range(m)]
ans2[f] = 1
for i in range(len(arr2)-1, -1, -1):
    flag = False
    for j in arr2[i]:
        if ans2[j] == 1:
            flag = True
            break
    if flag:
        for j in arr2[i]:
            if ans2[j] == 0:
                ans2[j] = 1
for i in range(m):
    print(ans2[i], end='')