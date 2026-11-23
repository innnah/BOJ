import sys
input = sys.stdin.readline

def simulation(distance):
    place = grass[0][0]
    cnt = 1
    for i in range(m):
        while place+distance <= grass[i][1]:
            place = max(place+distance, grass[i][0])
            cnt += 1
    return cnt

n, m = map(int, input().split())
grass = [list(map(int, input().split())) for _ in range(m)]
grass.sort()
ret = 0
lo, hi = 0, 10**50
while lo < hi:
    mid = (lo+hi)//2
    if simulation(mid) >= n:
        ret = mid
        lo = mid+1
    else:
        hi = mid
print(ret)