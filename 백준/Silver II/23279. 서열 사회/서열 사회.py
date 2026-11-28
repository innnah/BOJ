import sys
input = sys.stdin.readline

n, k = map(int, input().split())
for _ in range(k):
    m, *arr = list(map(int, input().split()))
    arr.sort()
    for i in range(m):
        arr[i] += i+1
    print(*arr)