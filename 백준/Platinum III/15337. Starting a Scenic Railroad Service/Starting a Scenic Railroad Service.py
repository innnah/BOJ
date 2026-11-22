import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    arr[i][1] -= 1

left = [arr[i][0] for i in range(n)]
right = [arr[i][1] for i in range(n)]

left.sort()
right.sort()

p1 = -1
for i in range(n):
    cand = n
    cand -= n - bisect.bisect(left, arr[i][1])
    cand -= bisect.bisect_left(right, arr[i][0])
    p1 = max(p1, cand)

psum = [0 for _ in range(100127)]
for i in range(n):
    psum[arr[i][0]] += 1
    psum[arr[i][1]+1] -= 1
for i in range(1, 100001):
    psum[i] += psum[i-1]
p2 = max(psum)

print(p1, p2)