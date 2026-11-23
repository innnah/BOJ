import sys, bisect
input = sys.stdin.readline

NEGINF = -98765432123456789
n, m, l = map(int, input().split())
shots = list(map(int, input().split()))
shots.sort()
animals = [list(map(int, input().split())) for _ in range(m)]
ret = 0
for i in animals:
    idx = bisect.bisect(shots, i[0]), bisect.bisect_left(shots, i[0])
    if idx[0] != idx[1]:
        ret += (i[1] <= l)
    else:
        if idx[0] != 0:
            left = shots[idx[0]-1]
        else:
            left = NEGINF
        if idx[0] != n:
            right = shots[idx[0]]
        else:
            right = NEGINF
        if abs(i[0]-left) + i[1] <= l or abs(i[0]-right) + i[1] <= l:
            ret += 1
print(ret)