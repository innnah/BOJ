import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    b = n//2+1
    ans = sum(arr[:b])
    cand = ans
    for i in range(b, n):
        cand = cand + arr[i] - arr[i-b]
        ans = min(cand, ans)
    print(ans, sum(arr)-ans)