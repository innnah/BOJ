import sys
from heapq import heappush, heappop
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    cnt = 1
    lq, rq = [], []
    l = []
    for _ in range((n+9)//10):
        l += list(map(int, input().split()))
    print(f"{(n+1)//2}\n")
    heappush(lq, (-l[0], l[0]))
    print(f"{l[0]} ")
    for i in range(1, n, 2):
        heappush(rq, l[i])
        heappush(lq, (-l[i+1], l[i+1]))
        if rq and lq:
            if lq[0][1] > rq[0]:
                v1, v2 = heappop(lq), heappop(rq)
                heappush(lq, (-v2, v2))
                heappush(rq, v1[1])
        print(f"{lq[0][1]} ")
        cnt += 1
        if cnt == 10:
            print("\n")
            cnt = 0
    print("\n")