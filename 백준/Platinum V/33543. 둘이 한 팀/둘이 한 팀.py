import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    ans += max(arr[i])

arr = [i[0]-i[1] for i in arr]
arr.sort()

psum = [0 for _ in range(n+1)]
for i in range(n):
    psum[i] = psum[i-1] + arr[i]

q = int(input())
add = 0
for _ in range(q):
    s, a = input().rstrip().split()
    a = int(a)
    if s == 'A':
        idx1 = bisect.bisect_left(arr, -a-add)
        idx2 = bisect.bisect_left(arr, -add)
        ans += (n-idx2) * a
        ans += (idx2-idx1)*a + (psum[idx2-1]-psum[idx1-1]) + add*(idx2-idx1)
    elif s == 'B':
        a = -a
        idx1 = bisect.bisect_left(arr, -add)
        idx2 = bisect.bisect_left(arr, -a-add)
        ans += idx1 * (-a)
        ans += (idx2-idx1)*(-a) - ((idx2-idx1)*add + psum[idx2-1]-psum[idx1-1])
    print(ans)
    add += a